from server import mcp


@mcp.resource("greeting://{name}")
def greet(name: str) -> str:
    """
    Returns a personalized greeting.

    Args:
        name: The name to include in the greeting.

    Returns:
        A greeting string.
    """
    return f"Hello, {name}!"


@mcp.resource("data://users")
def get_users() -> dict:
    """
    Returns a dictionary containing user data.

    Returns:
        A dictionary of users.
    """
    users = {
        "1": {"name": "Alice", "age": 30},
        "2": {"name": "Bob", "age": 25}
    }
    return users
