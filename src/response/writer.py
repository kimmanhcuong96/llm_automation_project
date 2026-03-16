
from pathlib import Path

RESPONSE_DIR = Path("responses")

def save_response(filename: str, content: str):
    RESPONSE_DIR.mkdir(exist_ok=True)
    path = RESPONSE_DIR / filename
    path.write_text(content, encoding="utf-8")
