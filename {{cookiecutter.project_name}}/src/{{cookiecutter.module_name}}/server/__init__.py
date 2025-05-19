import dotenv
from mcp.server.fastmcp import FastMCP

dotenv.load_dotenv()
mcp = FastMCP("{{ cookiecutter.project_title }}")
