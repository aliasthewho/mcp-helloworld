# MCP Hello World (Python)

Example [Model Context Protocol](https://modelcontextprotocol.io) servers written in Python, using the official `mcp` SDK. Both servers communicate over **stdio**.

## Servers

| File | Server name | Tool | Description |
|------|-------------|------|-------------|
| `weather_server.py` | `weather` | `get_weather(city)` | Current temperature, wind speed and conditions for a city, using the free [Open-Meteo](https://open-meteo.com) geocoding and forecast APIs (no API key needed). |
| `joke_server.py` | `joke` | `joke(topic)` | Minimal example tool that takes a topic. Currently a stub that returns an empty string. |

## Prerequisites

- Python 3.14 or newer (see `requires-python` in `pyproject.toml`)
- [uv](https://docs.astral.sh/uv/)
- [Claude Code](https://claude.com/claude-code) (to register the servers)

## Setup

Dependencies (`httpx`, `mcp[cli]`) are already declared in `pyproject.toml`:

```bash
cd python
uv sync
uv run python -c "import mcp; print('mcp OK')"
```

### How the project was created

```bash
# Create the project file (--bare creates only pyproject.toml, with no sample files)
uv init --bare

# Add the SDK. The cli extra adds the mcp command-line tools
uv add "mcp[cli]"
```

## Running a server

```bash
uv run weather_server.py
```

The server waits for MCP messages on stdin. In practice you register it with an MCP client instead (below).

> **Note:** never write to stdout from a stdio server, since it carries the protocol. Use `logging` (which writes to stderr) instead.

## Register with Claude Code

Replace `/path/to/MCP-HelloWorld` with the absolute path to this repository:

```bash
claude mcp add weather-python -- uv --directory /path/to/MCP-HelloWorld/python run weather_server.py
claude mcp add joke-python -- uv --directory /path/to/MCP-HelloWorld/python run joke_server.py
claude mcp list
```

Then ask Claude something like *"What's the weather in Madrid?"*

## Debugging

Use the MCP inspector from the `mcp[cli]` extra:

```bash
uv run mcp dev weather_server.py
```

The weather server logs each request (geocoding and forecast calls) to stderr with a `[weather]` prefix.
