from typing import Any
import httpx

from server import mcp

# Constants for NWS (National Weather Service) API
NWS_API_BASE = "https://api.weather.gov"
USER_AGENT = "weather-app/1.0"


async def make_nws_request(url: str) -> dict[str, Any] | None:
    """Make a request to the NWS API with proper error handling.

    This function handles the HTTP request to the NWS API, setting appropriate
    headers and handling potential errors during the request.

    Args:
        url: The complete URL for the NWS API endpoint

    Returns:
        A dictionary containing the JSON response if successful, None otherwise
    """
    # Set required headers for the NWS API
    headers = {
        "User-Agent": USER_AGENT,  # NWS API requires a user agent
        "Accept": "application/geo+json"  # Request GeoJSON format
    }
    # Create an async HTTP client
    async with httpx.AsyncClient() as client:
        try:
            # Make the GET request with timeout
            response = await client.get(url, headers=headers, timeout=30.0)
            response.raise_for_status()  # Raise exception for 4XX/5XX responses
            return response.json()  # Parse and return JSON response
        except Exception:
            # Return None if any error occurs (connection, timeout, parsing, etc.)
            return None


def format_alert(feature: dict) -> str:
    """Format an alert feature into a readable string.

    Extracts relevant information from a weather alert feature and formats it
    into a human-readable string.

    Args:
        feature: A dictionary containing a single weather alert feature

    Returns:
        A formatted string with key alert information
    """
    # Extract properties from the feature
    props = feature["properties"]
    # Format the alert with important details
    return f"""
Event: {props.get('event', 'Unknown')}
Area: {props.get('areaDesc', 'Unknown')}
Severity: {props.get('severity', 'Unknown')}
Description: {props.get('description', 'No description available')}
Instructions: {props.get('instruction', 'No specific instructions provided')}
"""


@mcp.tool()
async def get_alerts(state: str) -> str:
    """Get weather alerts for a US state.

    Fetches active weather alerts from the NWS API for a specified US state.

    Args:
        state: Two-letter US state code (e.g. CA, NY)

    Returns:
        A formatted string containing all active alerts for the state,
        or a message indicating no alerts or an error
    """
    # Construct the URL for the state's active alerts
    url = f"{NWS_API_BASE}/alerts/active/area/{state}"
    # Make the API request
    data = await make_nws_request(url)

    # Check if the response is valid
    if not data or "features" not in data:
        return "Unable to fetch alerts or no alerts found."

    # Check if there are any active alerts
    if not data["features"]:
        return "No active alerts for this state."

    # Format each alert and join them with separators
    alerts = [format_alert(feature) for feature in data["features"]]
    return "\n---\n".join(alerts)


@mcp.tool()
async def get_forecast(latitude: float, longitude: float) -> str:
    """Get weather forecast for a location.

    Fetches the weather forecast from the NWS API for a specified location
    using latitude and longitude coordinates.

    Args:
        latitude: Latitude of the location
        longitude: Longitude of the location

    Returns:
        A formatted string containing the forecast for the next 5 periods,
        or an error message if the forecast couldn't be retrieved
    """
    # First get the forecast grid endpoint using the coordinates
    points_url = f"{NWS_API_BASE}/points/{latitude},{longitude}"
    points_data = await make_nws_request(points_url)

    # Check if we received valid point data
    if not points_data:
        return "Unable to fetch forecast data for this location."

    # Extract the forecast URL from the points response
    # NWS API requires this two-step process to get the forecast
    forecast_url = points_data["properties"]["forecast"]
    forecast_data = await make_nws_request(forecast_url)

    # Check if we received valid forecast data
    if not forecast_data:
        return "Unable to fetch detailed forecast."

    # Extract and format the forecast periods
    periods = forecast_data["properties"]["periods"]
    forecasts = []
    for period in periods[:5]:  # Only show next 5 periods
        forecast = f"""
{period['name']}:
Temperature: {period['temperature']}°{period['temperatureUnit']}
Wind: {period['windSpeed']} {period['windDirection']}
Forecast: {period['detailedForecast']}
"""
        forecasts.append(forecast)

    # Join all forecast periods with separators
    return "\n---\n".join(forecasts)
