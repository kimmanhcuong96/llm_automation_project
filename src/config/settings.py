
import os
from pathlib import Path


def _load_env_file():
    # Lightweight ".env" loader so local config works without extra dependencies.
    env_path = Path(__file__).resolve().parents[2] / ".env"
    if not env_path.exists():
        return

    for raw_line in env_path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#"):
            continue
        if "=" not in line:
            continue
        key, value = line.split("=", 1)
        key = key.strip()
        value = value.strip().strip('"').strip("'")
        if key and key not in os.environ:
            os.environ[key] = value


_load_env_file()

# NOTE: This repo is a starter template. The default API_URL is intentionally a
# placeholder and will fail DNS resolution until you configure a real endpoint.
MODEL_NAME = os.getenv("MODEL_NAME", "gpt-4.1-mini")
API_URL = os.getenv("API_URL", "https://api.opengpt.example/chat")

# Supported values: "mock", "openai", "groq", "http"
# - mock: no network calls
# - openai: uses OpenAI Python SDK (requires OPENAI_API_KEY)
# - groq: uses OpenAI Python SDK against Groq OpenAI-compatible API (requires GROQ_API_KEY)
# - http: POST to API_URL with {"message": prompt} and expects {"response": "..."}
LLM_PROVIDER = os.getenv("LLM_PROVIDER", "").strip().lower()

def _parse_bool(value: str) -> bool:
    return value.strip().lower() in {"1", "true", "yes", "y"}


# If true, skip network calls and return a deterministic mock response.
# Default: enabled when API_URL is still the template placeholder so the project
# runs successfully out of the box.
_mock_env = os.getenv("MOCK_LLM")
if _mock_env is None:
    MOCK_LLM = "api.opengpt.example" in API_URL
else:
    MOCK_LLM = _parse_bool(_mock_env)

# Seconds
TIMEOUT = int(os.getenv("TIMEOUT", "30"))
