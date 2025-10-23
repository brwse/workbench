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

    try:
        # Create a frontend developer agent with MCP tools
        frontend_developer = Agent(
            role="Senior Frontend Developer",
            goal="Create a modern, responsive Next.js landing page with TypeScript and Tailwind CSS",
            backstory="You are an experienced frontend developer specializing in React and Next.js. You create beautiful, performant landing pages using the latest best practices. You MUST use the provided Workbench tools to write and manage files.",
            tools=tools,
            verbose=True,
            llm="claude-sonnet-4-5-20250929",
            allow_delegation=False,
        )

        # Define the landing page creation task
        task = Task(
            description="""
            Create a professional Next.js landing page for a SaaS product using the Workbench tools.

            Requirements:
            1. Set up a Next.js project structure with TypeScript and Tailwind CSS
            2. Create the following components in /workbench/landing-page/:
               - app/page.tsx: Main landing page with hero section, features, and CTA
               - app/layout.tsx: Root layout with metadata and global styles
               - app/globals.css: Tailwind CSS configuration
               - components/Hero.tsx: Hero section with headline and call-to-action
               - components/Features.tsx: Feature highlights section
               - components/CTA.tsx: Final call-to-action section
               - package.json: Dependencies for Next.js, React, TypeScript, and Tailwind
               - tailwind.config.ts: Tailwind configuration
               - tsconfig.json: TypeScript configuration
               - next.config.js: Next.js configuration

            3. The landing page should be for a fictional "AI Code Assistant" product
            4. Use modern design principles with a professional color scheme
            5. Make it fully responsive and accessible
            6. Include TypeScript types where appropriate

            Use absolute paths starting with /workbench/landing-page/
            Make the landing page visually appealing with gradients, proper spacing, and modern UI elements.
            """,
            expected_output="A complete Next.js landing page with all necessary files and components, ready to run",
            agent=frontend_developer,
        )

        # Create and run the crew
        crew = Crew(agents=[frontend_developer], tasks=[task], verbose=True)

        result = crew.kickoff()

        print("\n" + "=" * 60)
        print("✅ Landing page created successfully!")
        print("=" * 60)
        print(result)
        print("\n💡 To run the landing page:")
        print("   cd /workbench/landing-page")
        print("   npm install")
        print("   npm run dev")
    finally:
        tools["teardown_workbench"].run()
