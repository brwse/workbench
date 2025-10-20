# Workbench

**Workbench** is a cloud-based platform that provides AI agents with isolated, ephemeral development environments for executing code and file operations securely.

## What is Workbench?

Workbench implements the [Model Context Protocol (MCP)](https://modelcontextprotocol.io/) to enable AI models to interact with managed, sandboxed development environments. It acts as a gateway that:

- **Creates ephemeral instances** - Spins up temporary, isolated containers for each session
- **Proxies AI tool calls** - Routes MCP requests between AI agents and workbench instances
- **Manages sessions** - Handles lifecycle, monitoring, and cleanup with credit-based billing
- **Enforces constraints** - Applies customizable execution constraints for security and control
- **Provides dashboard UI** - Offers management interface for configuration and monitoring

## Key Features

### 🛠️ 11 MCP Tools

Workbench provides AI agents with powerful capabilities:

**Filesystem Operations:**
- `read` - Read file contents
- `write` - Create/overwrite files
- `edit` - Replace text in files
- `multi_edit` - Apply multiple edits atomically

**Search Operations:**
- `glob` - Find files by pattern
- `grep` - Search file contents with regex

**Execution Operations:**
- `bash` - Execute shell commands
- `bash_output` - Stream output from background processes
- `kill_shell` - Terminate running commands

**Session Management:**
- `init_workbench` - Initialize a workbench session
- `teardown_workbench` - Clean up a session

### 🔒 Profile & Constraint System

Create custom profiles to control agent behavior:

- **Custom tool descriptions** - Guide AI with contextual prompts
- **Execution limits** - Set timeouts, file size limits, output constraints
- **Path restrictions** - Allow/deny specific file paths with glob patterns
- **Command filtering** - Control which shell commands can be executed

### 💰 Usage-Based Billing

- Per-second credit consumption ($0.09/minute)
- Signup bonuses and credit purchases
- Auto-recharge options
- Session monitoring and cost tracking

### 🎯 Use Cases

- **Code Development** - Agents write, edit, and test code safely
- **File Operations** - Secure file manipulation with path constraints
- **Search & Analysis** - Search codebases with glob/grep
- **Command Execution** - Run builds, tests, deployments with protection
- **Multi-Agent Workflows** - Handle concurrent agent sessions

## Getting Started

### Prerequisites

- An AI agent or client that supports MCP (Model Context Protocol)
- A Workbench account (sign up at [workbench.brwse.ai](https://workbench.brwse.ai))

### Quick Start

1. **Sign up** for a Workbench account
2. **Generate an API key** from the dashboard
3. **Configure your MCP client** to connect to Workbench
4. **Create a profile** (optional) to customize tool behavior
5. **Start using** Workbench tools in your agent

### Example Agents

Check out our [examples](./examples) directory for working integrations:

- ✅ **[LangChain Integration](./examples/langchain)** - Complete example using `langchain-mcp-adapters`
- ✅ **[CrewAI Integration](./examples/crewai)** - Complete example using `MCPServerAdapter` from `crewai-tools`

#### Quick Start with LangChain

```bash
cd examples/langchain
uv sync
# Add your API keys to .env (WORKBENCH_API_KEY, ANTHROPIC_API_KEY)
uv run main.py
```

The LangChain example demonstrates:
- Executing bash commands in isolated environments
- Creating, editing, and reading files
- Writing and running Python scripts
- Multi-step agent reasoning with tool chaining

**All examples complete successfully end-to-end!**

#### Best Practice: Workbench Lifecycle

For better resource management, consider calling `init_workbench` before use and `teardown_workbench` when done:

```python
await session.call_tool("init_workbench")

try:
    # Your agent tasks here
    response = await agent.ainvoke(...)
finally:
    # Clean up resources
    await session.call_tool("teardown_workbench")
```

## Architecture

```
┌────────────────────────────────────┐
│  AI Clients (Claude, MCP clients)  │
└──────────────┬─────────────────────┘
               │ MCP Protocol (HTTP)
┌──────────────▼─────────────────────┐
│  Workbench Router (Go)             │
│  - MCP routing & proxying          │
│  - Session management              │
│  - Constraint enforcement          │
│  - Billing & credit tracking       │
└────┬──────────────────┬────────────┘
     │ gRPC             │ REST APIs
┌────▼────────┐    ┌───▼─────────────┐
│ Ephemeral   │    │ Dashboard (Web) │
│ Instances   │    │ - API Keys      │
│ (Containers)│    │ - Profiles      │
└─────────────┘    │ - Sessions      │
                   │ - Billing       │
                   └─────────────────┘
```

## Documentation

- **API Reference** - [Coming Soon]
- **Tool Specifications** - See issue templates for feature requests
- **Constraint System** - Learn about security and execution limits
- **Best Practices** - Tips for building agents with Workbench

## Community

- **Issues** - Report bugs or request features using our issue templates
- **Discussions** - Ask questions, share ideas, and connect with other users
- **Examples** - Contribute agent implementations for different frameworks

## Support

- **Documentation**: [docs.brwse.ai/workbench](https://docs.brwse.ai/workbench) (Coming Soon)
- **Dashboard**: [workbench.brwse.ai](https://workbench.brwse.ai)
- **Issues**: File bugs and feature requests on GitHub
- **Discussions**: Join our community discussions

---

Built with ❤️ by Brwse Co.
