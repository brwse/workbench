# Workbench Examples

This directory contains example integration patterns showing how to use Workbench with popular AI agent frameworks.

## Available Examples

### 1. [LangChain](./langchain/)
Integration example showing how to use Workbench tools within LangChain agents and chains.

**Best for:** Building complex agent workflows, RAG applications, multi-step reasoning

### 2. [CrewAI](./crewai/)
Example demonstrating Workbench integration with CrewAI for multi-agent collaboration.

**Best for:** Multi-agent systems, role-based task delegation, complex workflows

## Getting Started

Each example directory contains:
- `README.md` - Detailed setup and usage instructions
- `pyproject.toml` - Python project configuration and dependencies
- Working code examples
- Configuration templates
- `.env.example` - Environment variable template

## Prerequisites

1. **Workbench Account** - Sign up at [workbench.brwse.ai](https://workbench.brwse.ai)
2. **API Key** - Generate from the Workbench dashboard
3. **Python 3.10+** (for Python examples)
4. **[uv](https://docs.astral.sh/uv/)** - Fast Python package installer (recommended)

### Installing uv

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

## Quick Start

For any example:

```bash
cd examples/langchain    # or crewai
uv sync                  # Install dependencies
cp .env.example .env     # Copy environment template
# Edit .env with your API keys
uv run main.py           # Run an example
```

## Basic Usage Pattern

All examples follow a similar pattern:

1. **Install dependencies** with `uv sync`
2. **Configure authentication** with your Workbench API key in `.env`
3. **Initialize a Workbench session** using the `init_workbench` tool
4. **Use Workbench tools** (bash, read, write, etc.) in your agent
5. **Clean up** with `teardown_workbench` when done

## Environment Setup

Create a `.env` file in each example directory:

```bash
cp .env.example .env
# Edit .env with your keys:
# WORKBENCH_API_KEY=your_api_key_here
# WORKBENCH_MCP_URL=https://mcp.workbench.brwse.ai
```

## Contributing

Have an example using a different framework? We'd love to see it! Please:

1. Follow the structure of existing examples
2. Include a detailed README
3. Test your example thoroughly
4. Submit a pull request

## Support

- **Questions**: Open a [Discussion](https://github.com/yourusername/workbench/discussions)
- **Issues**: Report bugs in the [Issues](https://github.com/yourusername/workbench/issues) section
- **Documentation**: Visit [docs.brwse.ai/workbench](https://docs.brwse.ai/workbench)
