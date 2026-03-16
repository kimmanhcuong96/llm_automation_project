
import os

# NOTE: This repo is a starter template. The default API_URL is intentionally a
# placeholder and will fail DNS resolution until you configure a real endpoint.
MODEL_NAME = os.getenv("MODEL_NAME", "gpt-4")
API_URL = os.getenv("API_URL", "https://api.opengpt.example/chat")

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
