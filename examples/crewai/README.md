# Workbench CrewAI Example

This example demonstrates using Workbench MCP tools in a CrewAI crew via CrewAI's native MCP integration.

## Setup

```bash
uv sync
```

Configure `.env`:
```bash
WORKBENCH_API_KEY=your_workbench_api_key
ANTHROPIC_API_KEY=your_anthropic_api_key
```

## Examples

### 1. Calculator (calculator.py)
Creates a Python factorial calculator with tests.

```bash
uv run calculator.py
```

### 2. Next.js Landing Page (nextjs_landing_page.py)
Generates a complete Next.js landing page with TypeScript and Tailwind CSS.

```bash
uv run nextjs_landing_page.py
```

## Usage

```python
from crewai import Agent, Task, Crew
from crewai_tools import MCPServerAdapter

server_params = {
    "url": "https://mcp.workbench.brwse.ai",
    "transport": "streamable-http",
    "headers": {"X-API-Key": api_key},
}

with MCPServerAdapter(server_params) as tools:
    developer = Agent(
        role="Software Developer",
        tools=tools,
        llm=llm,
    )
    
    task = Task(
        description="Your task here",
        agent=developer,
    )
    
    crew = Crew(agents=[developer], tasks=[task])
    result = crew.kickoff()
```

## Learn More

- [CrewAI MCP Documentation](https://docs.crewai.com/en/mcp/overview)
- [Streamable HTTP Transport](https://docs.crewai.com/en/mcp/streamable-http)
- [Model Context Protocol](https://modelcontextprotocol.io/)
