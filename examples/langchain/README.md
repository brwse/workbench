# Workbench LangChain Example

This example demonstrates using Workbench MCP tools in a LangChain agent via `langchain-mcp-adapters`.

## Setup

```bash
uv sync
```

Configure `.env`:
```bash
WORKBENCH_API_KEY=your_workbench_api_key
ANTHROPIC_API_KEY=your_anthropic_api_key
```

## Run

```bash
uv run main.py
```

## Usage

```python
from langchain_mcp_adapters.client import MultiServerMCPClient
from langchain_mcp_adapters.tools import load_mcp_tools

client = MultiServerMCPClient({
    "workbench": {
        "url": "https://mcp.workbench.brwse.ai",
        "transport": "streamable_http",
        "headers": {"X-API-Key": api_key}
    }
})

async with client.session("workbench") as session:
    tools = await load_mcp_tools(session)
    await session.call_tool("init_workbench")

    try:
        agent = create_agent(llm, tools)
        response = await agent.ainvoke({"messages": [...]})
    finally:
        await session.call_tool("teardown_workbench")
```

## Learn More

- [LangGraph MCP Documentation](https://langchain-ai.github.io/langgraph/agents/mcp/)
- [Model Context Protocol](https://modelcontextprotocol.io/)
