# Contributing to Workbench

Thank you for your interest in contributing to Workbench! This document provides guidelines for contributing to this repository.

## What Can You Contribute?

This repository is for Workbench examples, documentation, and community discussions. You can contribute:

1. **Example Agents** - Implementations using different frameworks
2. **Documentation** - Improvements to guides and examples
3. **Bug Reports** - Issues with examples or documentation
4. **Feature Requests** - Suggestions for new examples or improvements
5. **Discussions** - Share ideas and help other users

**Note**: This repository does not contain the Workbench platform code itself, only examples and documentation.

## Getting Started

1. **Fork the repository**
2. **Clone your fork**:
   ```bash
   git clone https://github.com/yourusername/workbench.git
   cd workbench
   ```
3. **Create a branch**:
   ```bash
   git checkout -b feature/your-feature-name
   ```

## Contributing Examples

### Adding a New Example

If you want to add an example using a new framework:

1. **Create a directory** under `examples/`:
   ```bash
   mkdir examples/your-framework
   ```

2. **Include the following files**:
   - `README.md` - Comprehensive documentation
   - `pyproject.toml` - Python project configuration with dependencies
   - `.env.example` - Environment variable template
   - Example code files demonstrating key features

3. **Follow the structure** of existing examples:
   - Clear documentation with installation steps (using `uv sync`)
   - Multiple examples showing different use cases
   - Error handling and best practices
   - Comments explaining key concepts

4. **Test your example** thoroughly:
   - Verify all code runs successfully with `uv run`
   - Test with a real Workbench account
   - Check error handling works as expected
   - Ensure dependencies install correctly with `uv sync`

5. **Update the main examples README**:
   - Add your example to `examples/README.md`

### Example Structure Template

```
examples/your-framework/
├── README.md              # Comprehensive guide
├── pyproject.toml         # Project config and dependencies
├── .env.example          # Environment template
├── toolkit.py            # Framework integration
├── simple_example.py     # Basic example
├── advanced_example.py   # Advanced use case
└── ...                   # Additional examples
```

## Documentation Guidelines

### Writing Style

- **Be clear and concise** - Avoid jargon when possible
- **Include examples** - Show, don't just tell
- **Test all code** - Ensure all code samples work
- **Use proper formatting** - Follow markdown conventions

### Code Examples

```python
# Good: Clear, commented, complete example
from workbench import Client

# Initialize client with API key
client = Client(api_key="your_key")

# Create a session
session = client.init_workbench()

# Do work...
result = client.bash("echo 'Hello'")

# Always cleanup
client.teardown_workbench()
```

### README Template

Your example README should include:

1. **Title and brief description**
2. **Features** - What the example demonstrates
3. **Prerequisites** - Required tools (Python, uv) and accounts (Workbench, API keys)
4. **Installation** - Step-by-step setup using `uv sync`
5. **Usage** - How to run the examples with `uv run`
6. **Examples** - Multiple use cases
7. **Configuration** - Environment variables and options
8. **Troubleshooting** - Common issues and solutions
9. **Learn More** - Links to relevant documentation

### Installation Section Template

```markdown
## Installation

1. Install uv if you haven't already:

\`\`\`bash
curl -LsSf https://astral.sh/uv/install.sh | sh
\`\`\`

2. Sync dependencies:

\`\`\`bash
uv sync
\`\`\`

3. Set up environment variables:

\`\`\`bash
cp .env.example .env
# Edit .env with your API keys
\`\`\`
```

## Submitting Changes

### Pull Request Process

1. **Update documentation** - If you change functionality
2. **Test thoroughly** - Ensure everything works
3. **Commit with clear messages**:
   ```bash
   git commit -m "Add LlamaIndex integration example"
   ```
4. **Push to your fork**:
   ```bash
   git push origin feature/your-feature-name
   ```
5. **Create a Pull Request** with:
   - Clear title describing the change
   - Description of what you added/changed
   - Testing steps you performed
   - Screenshots/examples if applicable

### Commit Message Guidelines

- Use present tense ("Add feature" not "Added feature")
- Use imperative mood ("Move cursor to..." not "Moves cursor to...")
- Limit first line to 72 characters
- Reference issues and PRs when relevant

Examples:
```
Add Semantic Kernel integration example
Fix typo in LangChain README
Update installation instructions for Python 3.11
```

## Code Style

### Python

- Follow [PEP 8](https://pep8.org/)
- Use meaningful variable names
- Include docstrings for functions and classes
- Add type hints when possible
- Maximum line length: 88 characters (Black default)

### JavaScript/TypeScript

- Use 2 spaces for indentation
- Use semicolons
- Prefer `const` over `let`
- Use meaningful variable names
- Include JSDoc comments

## Reporting Issues

### Bug Reports

Use the bug report template and include:

- Clear description of the issue
- Steps to reproduce
- Expected vs actual behavior
- Environment details (OS, Python version, etc.)
- Error messages or logs
- Screenshots if applicable

### Feature Requests

Use the feature request template and include:

- Problem you're trying to solve
- Proposed solution
- Use case description
- Alternative approaches considered

## Community Guidelines

- **Be respectful** - Treat everyone with respect
- **Be constructive** - Provide helpful feedback
- **Be patient** - Remember everyone is learning
- **Ask questions** - No question is too simple
- **Share knowledge** - Help others when you can

## Getting Help

- **Discussions** - Ask questions in GitHub Discussions
- **Issues** - Report bugs or request features
- **Documentation** - Check [docs.brwse.ai/workbench](https://docs.brwse.ai/workbench)
- **Examples** - Review existing examples in this repo

## Recognition

Contributors will be:
- Listed in the repository contributors
- Mentioned in release notes for significant contributions
- Credited in documentation for major examples

## License

By contributing, you agree that your contributions will be licensed under the same license as the project (MIT License).

## Questions?

If you have questions about contributing, please:
- Open a discussion in the GitHub Discussions section
- Reach out in the community channels
- Review existing issues and PRs for similar questions

Thank you for contributing to Workbench! 🎉
