import logging

import httpx
from mcp.server.mcpserver import MCPServer

# basicConfig writes to stderr by default. NEVER log to stdout: it carries the protocol.
logging.basicConfig(level=logging.INFO, format="[weather] %(levelname)s %(message)s")
log = logging.getLogger("weather")

mcp = MCPServer("weather")

GEOCODING_URL = "https://geocoding-api.open-meteo.com/v1/search"
FORECAST_URL = "https://api.open-meteo.com/v1/forecast"

# WMO weather interpretation codes used by Open-Meteo
WMO_CODES = {
    0: "clear sky",
    1: "mainly clear",
    2: "partly cloudy",
    3: "overcast",
    45: "fog",
    48: "rime fog",
    51: "light drizzle",
    53: "drizzle",
    55: "heavy drizzle",
    56: "light freezing drizzle",
    57: "freezing drizzle",
    61: "light rain",
    63: "rain",
    65: "heavy rain",
    66: "light freezing rain",
    67: "freezing rain",
    71: "light snow",
    73: "snow",
    75: "heavy snow",
    77: "snow grains",
    80: "light rain showers",
    81: "rain showers",
    82: "violent rain showers",
    85: "light snow showers",
    86: "snow showers",
    95: "thunderstorm",
    96: "thunderstorm with hail",
    99: "thunderstorm with heavy hail",
}

@mcp.tool()
async def get_weather(city: str) -> str:
    """Get the current weather for a city."""
    log.info("get_weather called with city=%r", city)
    try:
        async with httpx.AsyncClient(timeout=10.0) as client:
            geo = await client.get(GEOCODING_URL, params={"name": city, "count": 1})
            log.info("geocoding -> HTTP %s %s", geo.status_code, geo.url)
            geo.raise_for_status()
            results = geo.json().get("results")
            if not results:
                log.warning("geocoding returned no results for %r", city)
                return f"City not found: {city}"

            place = results[0]
            log.info("resolved to %s (%s, %s)", place["name"], place["latitude"], place["longitude"])
            forecast = await client.get(
                FORECAST_URL,
                params={
                    "latitude": place["latitude"],
                    "longitude": place["longitude"],
                    "current": "temperature_2m,wind_speed_10m,weather_code",
                },
            )
            log.info("forecast -> HTTP %s %s", forecast.status_code, forecast.url)
            forecast.raise_for_status()
            current = forecast.json()["current"]
            log.info("raw current data: %s", current)
    except httpx.HTTPError as exc:
        log.error("Open-Meteo request failed: %s", exc)
        return f"Weather service unavailable: {exc}"

    conditions = WMO_CODES.get(current["weather_code"], "unknown conditions")
    return (
        f"{place['name']}: {current['temperature_2m']}°C, "
        f"wind {current['wind_speed_10m']} km/h, {conditions}"
    )

if __name__ == "__main__":
    mcp.run(transport="stdio")