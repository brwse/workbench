#!/usr/bin/env python3
"""
Simple LangChain Agent with Workbench MCP Tools

Demonstrates using Workbench tools in a LangChain agent via MCP.
"""

import os
import asyncio
from dotenv import load_dotenv
from langchain_mcp_adapters.client import MultiServerMCPClient
from langchain_mcp_adapters.tools import load_mcp_tools
from langchain.agents import create_agent
from langchain_anthropic import ChatAnthropic

load_dotenv()


async def main():
    """Run a simple agent with Workbench tools."""

    api_key = os.getenv("WORKBENCH_API_KEY")
    mcp_url = os.getenv("WORKBENCH_MCP_URL", "https://mcp.workbench.brwse.ai")

    if not api_key:
        raise ValueError("WORKBENCH_API_KEY not set")

    # Configure Workbench as an MCP server
    client = MultiServerMCPClient(
        {
            "workbench": {
                "url": mcp_url,
                "transport": "streamable_http",
                "headers": {"X-API-Key": api_key},
            }
        }
    )

    # Start explicit session and load tools
    print("Connecting to Workbench and starting session...")
    async with client.session("workbench") as session:
        print("✓ Session started")

        print("\nLoading tools...")
        tools = await load_mcp_tools(session)
        print(f"✓ Loaded {len(tools)} tools from Workbench")

        print("\nInitializing workbench...")
        await session.call_tool("init_workbench")
        print("\n✓ Workbench created")

        try:
            # Create agent with Anthropic Claude
            print("\nCreating agent...")
            llm = ChatAnthropic(
                model_name="claude-haiku-4-5-20251001", timeout=60, stop=[]
            )
            agent = create_agent(
                llm,
                tools,
            )
            print("✓ Agent created")

            # Example 1: Simple bash command
            print("\n" + "=" * 60)
            print("Example 1: Running a bash command")
            print("=" * 60)
            response = await agent.ainvoke(
                {
                    "messages": [
                        {
                            "role": "user",
                            "content": "Use bash to print 'Hello from Workbench!' and show me the current date",
                        }
                    ]
                }
            )
            print(f"Agent response: {response['messages'][-1].content}")

            # Example 2: File operations
            print("\n" + "=" * 60)
            print("Example 2: Creating and reading a file")
            print("=" * 60)
            await session.call_tool("bash", {"command": "rm -rf /workbench/hello.txt"})
            response = await agent.ainvoke(
                {
                    "messages": [
                        {
                            "role": "user",
                            "content": "Write a file called /workbench/hello.txt with the content 'Hello World', then read it back to verify",
                        }
                    ]
                }
            )
            print(f"Agent response: {response['messages'][-1].content}")

            # Example 3: Complex task
            print("\n" + "=" * 60)
            print("Example 3: Multi-step task")
            print("=" * 60)
            await session.call_tool(
                "bash", {"command": "rm -rf /workbench/fibonacci.py"}
            )
            response = await agent.ainvoke(
                {
                    "messages": [
                        {
                            "role": "user",
                            "content": "Write a Python script at /workbench/fibonacci.py that prints the first 10 fibonacci numbers, then run it",
                        }
                    ]
                }
            )
            print(f"Agent response: {response['messages'][-1].content}")

            print("\n✅ All examples completed!")

        finally:
            # Always tear down workbench, even on failure
            print("\nTearing down workbench...")
            try:
                await session.call_tool("teardown_workbench")
                print("✓ Workbench torn down")
            except Exception as e:
                print(f"⚠ Error during teardown: {e}")


if __name__ == "__main__":
    asyncio.run(main())
