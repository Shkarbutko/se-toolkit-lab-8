import json
import os
import sys
from pathlib import Path

config_path = Path("/app/nanobot/config.json")
resolved_path = Path("/app/nanobot/config.resolved.json")

data = json.loads(config_path.read_text())

defaults = data.setdefault("agents", {}).setdefault("defaults", {})
defaults["model"] = os.getenv("LLM_API_MODEL", "coder-model")
defaults["provider"] = "openai"

providers = data.setdefault("providers", {})
providers.setdefault("openai", {})
providers["openai"]["apiKey"] = os.getenv("LLM_API_KEY", "sk-local-test")
providers["openai"]["apiBase"] = os.getenv("LLM_API_BASE_URL", "http://qwen-code-api:4000/v1")

gateway = data.setdefault("gateway", {})
gateway["host"] = os.getenv("NANOBOT_GATEWAY_CONTAINER_ADDRESS", "0.0.0.0")
gateway["port"] = int(os.getenv("NANOBOT_GATEWAY_CONTAINER_PORT", "8080"))

tools = data.setdefault("tools", {}).setdefault("mcpServers", {})
tools.setdefault("lms", {})
tools["lms"] = {
    "command": "python",
    "args": ["-m", "mcp_lms"],
    "env": {
        "NANOBOT_LMS_BACKEND_URL": os.getenv("NANOBOT_LMS_BACKEND_URL", "http://backend:8000"),
        "NANOBOT_LMS_API_KEY": os.getenv("NANOBOT_LMS_API_KEY", os.getenv("LMS_API_KEY", "my-secret-key")),
    },
}

resolved_path.write_text(json.dumps(data, indent=2))

os.execvp(
    "uv",
    [
        "uv",
        "run",
        "nanobot",
        "gateway",
        "--config",
        str(resolved_path),
        "--workspace",
        "/app/nanobot/workspace",
    ],
)
