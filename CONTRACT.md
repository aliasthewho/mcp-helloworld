# MCP Weather Server: Shared Contract

Goal: learn MCP concepts by building the **same** server in several languages,
then compare them. Every implementation MUST follow this contract so the
comparison is fair.

## Layout

```
MCP-HelloWorld/
├── CONTRACT.md
├── python/   uv + official Python SDK
├── java/     Maven + official Java SDK
└── go/       Go modules + official Go SDK
```

Build order: Python, then Java, then Go.

## Server

| Item | Value |
|---|---|
| Server name | `weather` |
| Transport | stdio (the host launches the server as a subprocess) |
| Client for testing | Claude Code |
| Registered as | `weather-python`, `weather-java`, `weather-go` |
| External API | Open-Meteo (no API key) |

## Tool: `get_weather`

- **Description (shown to the LLM):** "Get the current weather for a city."
- **Input:** `city` (string, required)
- **Flow:**
  1. Geocoding: `https://geocoding-api.open-meteo.com/v1/search?name=<city>&count=1`
  2. Forecast: `https://api.open-meteo.com/v1/forecast?latitude=<lat>&longitude=<lon>&current=temperature_2m,wind_speed_10m,weather_code`
- **Success output (text):** `Madrid: 18.2°C, wind 12.0 km/h, partly cloudy`
- **City not found:** `City not found: <city>`

## Out of scope (YAGNI)

No 5-minute refresh loop, no cache, no resources, no prompts, no notifications,
no auth, no HTTP transport. Possible later additions: a second tool, a prompt,
a custom Python client (e.g. with an Ollama model).

## Build steps (per language)

1. Project setup
2. Fake `hello` tool, to prove the plumbing
3. Register in Claude Code and call it
4. Replace with the real `get_weather`

Each step is confirmed working before moving to the next.

## Comparison at the end

Raw facts only (lines of code, setup steps, restart/build time). The weighting
is the user's own.
