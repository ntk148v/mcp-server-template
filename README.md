<div align="center">
    <h1>MCP Server Cookiecutter template</h1>
    <p>A <a src="https://github.com/cookiecutter/cookiecutter">Cookiecutter</a> template for creating <a src="https://modelcontextprotocol.io/">Model Context Protocol (MCP)</a> servers with Python.</p>
    <p>
        <a href="https://github.com/ntk148v/mcp-server-template/blob/master/LICENSE">
            <img alt="GitHub license" src="https://img.shields.io/github/license/ntk148v/mcp-server-template?style=for-the-badge">
        </a>
    <a href="https://github.com/ntk148v/mcp-server-template/stargazers">
        <img alt="GitHub stars" src="https://img.shields.io/github/stars/ntk148v/mcp-server-template?style=for-the-badge">
    </a>
</div>

Table of contents:
- [1. Introduction](#1-introduction)
- [2. Quickstart](#2-quickstart)
  - [2.1. Requirements](#21-requirements)
  - [2.2. Create a project](#22-create-a-project)
  - [2.3. Getting started with your new server](#23-getting-started-with-your-new-server)
- [3. License](#3-license)


## 1. Introduction

- This template provides you a easy managable way to create your own MCP server. MCP servers can expose:
  - **Tools**: Functions that LLMs can execute to perform actions
  - **Resources**: Data sources that LLMs can access for context
  - **Prompts**: Reusable templates for LLM interactions
- Features:
  - [x] Complete project structure with all necessary components pre-configured
  - [x] Configurable transport modes (stdio, SSE)
  - [x] Suport tools, resources and prompts.
  - [x] Docker support for containerized deployment
  - [x] FastMCP integration for simple decorator-based development
  - [x] Github actions
  - [x] Minimal dependencies

## 2. Quickstart

### 2.1. Requirements

- Python 3.12
- Cookiecutter

### 2.2. Create a project

```shell
# Generate a new MCP server project from the template
cookiecutter gh:ntk148v/mcp-server-template

# Or from local copy
cookiecutter path/to/mcp-server-template

# Enter your desired input
```

### 2.3. Getting started with your new server

- File structure:

```shell
{{cookiecutter.project_name}}
├── Dockerfile
├── .github
│   └── workflows
│       ├── docker.yaml
│       └── publish.yaml
├── .gitignore
├── LICENSE
├── Makefile
├── pyproject.toml
├── README.md
├── src
│   └── {{cookiecutter.module_name}}
│       ├── __init__.py
│       ├── main.py
│       └── server
│           ├── __init__.py
│           ├── prompts
│           │   ├── __init__.py
│           │   └── prompts.py
│           ├── resources
│           │   ├── __init__.py
│           │   └── resources.py
│           └── tools
│               ├── __init__.py
│               └── tools.py
└── tests
    └── .gitkeep
```

|                      |                                                                           |
| -------------------- | ------------------------------------------------------------------------- |
| `main.py`            | Main configuration                                                        |
| `server/__init__.py` | Init FastMCP server                                                       |
| `server/tools`       | Tool implementations (functions that the LLM can call to perform actions) |
| `server/resources`   | Resource implementations (data sources that provide context to the LLM)   |
| `server/prompts`     | Prompt template implementations (reusable conversation templates)         |
| `tests/`             | Test cases                                                                |

- Edit these files according to your need: adding a new tool, a new resource, ...
- Run dev mode for testing:

```shell
$ make dev
```

- Install in Claude Desktop:

```shell
$ make install
```

## 3. License

[Apache 2.0](LICENSE)

---

<div align="center">
    <sub>Made with ❤️ by <a href="https://github.com/ntk148v">@ntk148v</a></sub>
</div>
