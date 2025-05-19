FROM python:3.12-slim-bookworm AS builder
COPY --from=ghcr.io/astral-sh/uv:latest /uv /usr/local/bin/uv
WORKDIR /app
ENV UV_COMPILE_BYTECODE=1
COPY pyproject.toml uv.lock ./
COPY src ./src/
RUN uv venv && uv pip install --no-cache-dir -e .

FROM python:3.12-slim-bookworm
WORKDIR /app
COPY --from=ghcr.io/astral-sh/uv:latest /uv /usr/local/bin/uv
RUN groupadd -r app && useradd -r -g app app
COPY --from=builder /app/.venv /app/.venv
COPY --from=builder /app/src /app/src
COPY pyproject.toml ./
ENV PATH="/app/.venv/bin:$PATH" \
    PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONPATH="/app" \
    PYTHONFAULTHANDLER=1
USER app
EXPOSE 8000
HEALTHCHECK --interval=30s --timeout=5s --start-period=5s --retries=3 \
    CMD curl -f http://localhost:8000/health || exit 1
CMD ["/app/.venv/bin/{{ cookiecutter.project_name }}"]

LABEL org.opencontainers.image.title="{{ cookiecutter.project_title }}" \
    org.opencontainers.image.description="{{ cookiecutter.project_description }}" \
    org.opencontainers.image.version="{{ cookiecutter.version }}" \
    org.opencontainers.image.authors="{{ cookiecutter.author_name }} <{{ cookiecutter.author_email }}>" \
    org.opencontainers.image.source="https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_name }}" \
    org.opencontainers.image.licenses="Apache 2" \
    org.opencontainers.image.url="https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_name }}" \
    org.opencontainers.image.documentation="https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_name }}#readme"
