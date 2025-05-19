# -*- coding: utf-8 -*-
from mcp.server import Server
from mcp.server.sse import SseServerTransport
from starlette.applications import Starlette
from starlette.requests import Request
from starlette.routing import Mount, Route
import uvicorn

from .server import mcp


def create_starlette_app(mcp_server: Server, *, debug: bool = False) -> Starlette:
    """Create a Starlette application that can serve the provided MCP server with SSE.

    Sets up a Starlette web application with routes for SSE (Server-Sent Events)
    communication with the MCP server.

    Args:
        mcp_server: The MCP server instance to connect
        debug: Whether to enable debug mode for the Starlette app

    Returns:
        A configured Starlette application
    """
    # Create an SSE transport with a base path for messages
    sse = SseServerTransport("/messages/")

    async def handle_sse(request: Request) -> None:
        """Handler for SSE connections.

        Establishes an SSE connection and connects it to the MCP server.

        Args:
            request: The incoming HTTP request
        """
        # Connect the SSE transport to the request
        async with sse.connect_sse(
                request.scope,
                request.receive,
                request._send,  # noqa: SLF001
        ) as (read_stream, write_stream):
            # Run the MCP server with the SSE streams
            await mcp_server.run(
                read_stream,
                write_stream,
                mcp_server.create_initialization_options(),
            )

    # Create and return the Starlette application with routes
    return Starlette(
        debug=debug,
        routes=[
            Route("/sse", endpoint=handle_sse),  # Endpoint for SSE connections
            # Endpoint for posting messages
            Mount("/messages/", app=sse.handle_post_message),
        ],
    )


if __name__ == "__main__":
    # Get the underlying MCP server from the FastMCP instance
    mcp_server = mcp._mcp_server  # noqa: WPS437

    import argparse

    # Set up command-line argument parsing
    parser = argparse.ArgumentParser(
        description='Run MCP server with configurable transport')
    # Allow choosing between stdio and SSE transport modes
    parser.add_argument('--transport', choices=['stdio', 'sse'], default='stdio',
                        help='Transport mode (stdio or sse)')
    # Host configuration for SSE mode
    parser.add_argument('--host', default='0.0.0.0',
                        help='Host to bind to (for SSE mode)')
    # Port configuration for SSE mode
    parser.add_argument('--port', type=int, default=8080,
                        help='Port to listen on (for SSE mode)')
    args = parser.parse_args()

    # Launch the server with the selected transport mode
    if args.transport == 'stdio':
        # Run with stdio transport (default)
        # This mode communicates through standard input/output
        mcp.run(transport='stdio')
    else:
        # Run with SSE transport (web-based)
        # Create a Starlette app to serve the MCP server
        starlette_app = create_starlette_app(mcp_server, debug=True)
        # Start the web server with the configured host and port
        uvicorn.run(starlette_app, host=args.host, port=args.port)
