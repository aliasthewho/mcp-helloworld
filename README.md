# MCP HelloWorld: Weather Server

A learning project for the [Model Context Protocol](https://modelcontextprotocol.io) (MCP). The
same small **weather** server is built in several languages, each using its official SDK, so the
implementations can be compared fairly.

## What the server does

It exposes one tool, `get_weather`, over stdio:

- **Input:** `city` (string)
- **Output:** current weather for that city, e.g. `Madrid: 18.2°C, wind 12.0 km/h, partly cloudy`
- If the city is unknown: `City not found: <city>`

Data comes from [Open-Meteo](https://open-meteo.com) (geocoding + forecast), which needs no API key.
[Claude Code](https://claude.com/claude-code) is used as the test client.

## Layout

| Directory | Stack | Status |
|---|---|---|
| `python/` | uv + official Python SDK | In progress (project setup) |
| `java/` | Maven + official Java SDK | Planned |
| `go/` | Go modules + official Go SDK | Planned |

Build order: Python, then Java, then Go.

## Contract

All implementations must follow [CONTRACT.md](CONTRACT.md), which defines the server name, transport,
tool description, API flow, output format, and what is out of scope.

## Getting started (Python)

Requires Python 3.14+ and [uv](https://docs.astral.sh/uv/).

```bash
cd python
uv sync
```

Once the server is implemented, register it in Claude Code as `weather-python`.
