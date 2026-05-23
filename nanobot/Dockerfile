FROM ghcr.io/astral-sh/uv:python3.14-bookworm-slim

ENV UV_HTTP_TIMEOUT=300
ENV UV_LINK_MODE=copy

WORKDIR /app

COPY pyproject.toml uv.lock ./
COPY nanobot/ /app/nanobot
COPY mcp/ /app/mcp
COPY nanobot-websocket-channel/ /app/nanobot-websocket-channel

WORKDIR /app/nanobot

RUN --mount=type=cache,target=/root/.cache/uv uv sync

CMD ["python", "/app/nanobot/entrypoint.py"]
