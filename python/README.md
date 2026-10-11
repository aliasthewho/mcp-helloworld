
## Create the project file (--bare creates only pyproject.toml, with no sample files) 
# uv init --bare

## Add the SDK. CLI  extra adds the mcp command-line tools
# uv add "mcp[cli]"

## Check that it imports
# uv run python -c "import mcp; print('mcp OK')"


### Register MCP


* claude mcp add weather-python -- uv --directory /Users/miguel/Documents/MCP-HelloWorld/python run weather_server.py
* claude mcp list