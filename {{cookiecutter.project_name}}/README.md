<div align="center">
    <h1>{{ cookiecutter.project_title }}</h1>
    <p>
        <a href="https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_name }}/blob/master/LICENSE">
            <img alt="GitHub license" src="https://img.shields.io/github/license/{{ cookiecutter.github_username }}/{{ cookiecutter.project_name }}?style=for-the-badge">
        </a>
    <a href="https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_name }}/stargazers">
        <img alt="GitHub stars" src="https://img.shields.io/github/stars/{{ cookiecutter.github_username }}/{{ cookiecutter.project_name }}?style=for-the-badge">
    </a>
</div>

## Table of Contents
- [Table of Contents](#table-of-contents)
- [1. Introduction](#1-introduction)
- [2. Features](#2-features)
- [3. Quickstart](#3-quickstart)
  - [3.1. Prerequisites](#31-prerequisites)
  - [3.2. Local Run](#32-local-run)
- [4. Tools](#4-tools)
- [5. Development](#5-development)
- [6. License](#6-license)

> [!Important]
> Don't forget to update README with your content.

## 1. Introduction
## 2. Features

## 3. Quickstart

### 3.1. Prerequisites

- Python 3.12+
- [uv](https://github.com/astral-sh/uv) (for fast dependency management).
- Docker (optional, for containerized deployment).

### 3.2. Local Run

- Clone the repository:

```bash
# Clone the repository
$ git clone https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_name }}.git
```

- Add the server configuration to your client configuration file. For example, for Claude Desktop:

```json
{
  "mcpServers": {
    "{{ cookiecutter.project_name }}": {
      "command": "uv",
      "args": [
        "--directory",
        "<full path to {{ cookiecutter.project_name }} directory>",
        "run",
        "src/{{ cookiecutter.module_name }}/main.py"
      ],
      "env": {
      }
    }
  }
}
```s

### 3.3. Docker Run

- Run it with pre-built image (or you can build it yourself):

```bash
$ docker run -p 8000:8000 ghcr.io/{{ cookiecutter.github_username }}/{{ cookiecutter.project_name }}
```

- Running with Docker in Claude Desktop:

```json
{
  "mcpServers": {
    "{{ cookiecutter.project_name }}": {
      "command": "docker",
      "args": [
        "run",
        "--rm",
        "-i",
        "ghcr.io/{{ cookiecutter.github_username }}/{{ cookiecutter.project_name }}:latest"
      ],
      "env": {
      }
    }
  }
}
```

This configuration passes the environment variables from Claude Desktop to the Docker container by using the `-e` flag with just the variable name, and providing the actual values in the `env` object.

## 4. Tools

## 5. Development

Contributions are welcome! Please open an issue or submit a pull request if you have any suggestions or improvements.

This project uses [uv](https://github.com/astral-sh/uv) to manage dependencies. Install uv following the instructions for your platform.

```bash
# Clone the repository
$ git clone https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_name }}.git
$ cd {{ cookiecutter.project_name }}
$ make setup
# Run test
$ make test
# Run in development mode
$ mcp dev
$ TRANSPORT_MODE=sse mcp dev

# Install in Claude Desktop
$ make install
```

## 6. License

[Apache 2.0](LICENSE)

---

<div align="center">
    <sub>Made with ❤️ by <a href="https://github.com/{{ cookiecutter.github_username }}">@{{ cookiecutter.github_username }}</a></sub>
</div>
