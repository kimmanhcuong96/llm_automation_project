
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]
RESPONSE_DIR = PROJECT_ROOT / "responses"

def save_response(filename: str, content: str):
    RESPONSE_DIR.mkdir(exist_ok=True)
    path = RESPONSE_DIR / filename
    path.write_text(content, encoding="utf-8")
