import os
from dotenv import load_dotenv
from crewai import Agent, Task, Crew
from crewai_tools import MCPServerAdapter

load_dotenv()

api_key = os.getenv("WORKBENCH_API_KEY")
mcp_url = os.getenv("WORKBENCH_MCP_URL", "https://mcp.workbench.brwse.ai")
anthropic_api_key = os.getenv("ANTHROPIC_API_KEY")

if not api_key:
    raise ValueError("WORKBENCH_API_KEY environment variable is required")
if not anthropic_api_key:
    raise ValueError("ANTHROPIC_API_KEY environment variable is required")

os.environ["ANTHROPIC_API_KEY"] = anthropic_api_key

# Configure Workbench MCP server
server_params = {
    "url": mcp_url,
    "transport": "streamable-http",
    "headers": {"X-API-Key": api_key},
}

print("🚀 Starting CrewAI with Workbench MCP tools...")

# Use MCPServerAdapter to load Workbench tools
with MCPServerAdapter(server_params) as tools:
    print(f"✅ Connected to Workbench. Available tools: {len(tools)}")

    # Create an agent with MCP tools
    developer = Agent(
        role="Software Developer",
        goal="Write and test Python code in an isolated environment",
        backstory="You are an experienced Python developer who uses the Workbench environment to safely write and test code.",
        tools=tools,
        verbose=True,
        llm="claude-haiku-4-5-20251001",
    )

    # Define a task
    task = Task(
        description="""
        Create a Python script that calculates the factorial of a number.

        Steps:
        1. Write a file at /workbench/factorial.py with a factorial function
        2. Create a test file at /workbench/test_factorial.py that tests the function
        3. Run the test using bash to verify it works

        Use absolute paths starting with /workbench/
        """,
        expected_output="A working factorial implementation with passing tests",
        agent=developer,
    )

    # Create and run the crew
    crew = Crew(agents=[developer], tasks=[task], verbose=True)

    result = crew.kickoff()

    print("\n" + "=" * 60)
    print("✅ Task completed successfully!")
    print("=" * 60)
    print(result)
