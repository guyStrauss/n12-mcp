# n12-mcp

**Proof of concept for MCP**

## Purpose

This project demonstrates a proof of concept for using the Model Context Protocol (MCP) to expose N12 news content through a lightweight Python service, enabling integration with LLM frontends.

## Prerequisites

- Python 3.12 or newer
- [uv](https://github.com/astral-sh/uv) CLI installed (fast Python package manager)
- (Optional) [Claude Desktop](https://modelcontextprotocol.io/quickstart/server) for MCP host testing

## Installation

1. Create and activate a Python virtual environment (recommended):
   ```bash
   python3.12 -m venv .venv
   source .venv/bin/activate
   ```

2. Install the `uv` CLI if not already available:
   ```bash
   pip install uv
   ```

3. Install project dependencies from `pyproject.toml` and `uv.lock`:
   ```bash
   uv sync
   ```

## Usage

Inspect the MCP service by running the server entrypoint:
```bash
mcp dev src/server.py
```
This starts the local MCP host on the default port, ready to serve news queries.

## Testing with Claude Desktop

To connect your `n12-mcp` server to Claude Desktop as an MCP host, follow the official quickstart: https://modelcontextprotocol.io/quickstart/server

1. Ensure Claude Desktop is installed and up to date.
2. Open or create the configuration file:
   - macOS/Linux: `~/Library/Application Support/Claude/claude_desktop_config.json`
   - Windows: `%AppData%\Claude\claude_desktop_config.json`

3. Add your server under the `mcpServers` key. Example configuration:
```json
{
  "mcpServers": {
      "news": {
          "command": "<PATH_TO_UV>",
          "args": [
              "--directory",
              "<PATH_TO_REPO>/src/",
              "run",
              "server.py"
          ]
      }
  }
}
```
4. Restart Claude Desktop. You should now see and interact with the `n12-mcp` host in the Claude UI.
