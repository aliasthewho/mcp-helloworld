from mcp.server.mcpserver import MCPServer

mcp = MCPServer("joke")

@mcp.tool
def joke(topic: str) -> str:
    """Say a joke related to the topic"""
    return f""

if __name__ == "__main__":
    mcp.run(transport="stdio")