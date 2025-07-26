from mcp.server.fastmcp import FastMCP

mcp= FastMCP("Weather")

@mcp.tool()
async def get_weather(location: str) -> str:
    """Fetches the current weather for a given location."""
    # Simulate fetching weather data
    return f"The current weather in {location} is sunny with a temperature of 25°C."

if __name__ == "__main__":
    mcp.run(transport="streamable-http")  # Use "http" for HTTP transport or "stdio" for standard input/output