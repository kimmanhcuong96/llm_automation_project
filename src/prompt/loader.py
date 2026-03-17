from pathlib import Path
import os

PROJECT_ROOT = Path(__file__).resolve().parents[2]
PROMPT_DIR = PROJECT_ROOT / "prompts"


def load_prompt(filename: str) -> str:
    # Allow passing either "foo.txt" (resolved under prompts/) or any real path.
    candidate = Path(filename)
    path = candidate if candidate.exists() else (PROMPT_DIR / filename)
    if not path.exists():
        raise FileNotFoundError(
            f"Prompt file not found: {path}. Current working directory is {Path.cwd()}."
        )

    text = path.read_text(encoding="utf-8")
    if os.getenv("PRINT_PROMPT", "").strip().lower() in {"1", "true", "yes", "y"}:
        # Avoid crashing on Windows consoles that can't encode certain Unicode characters.
        try:
            print(text)
        except UnicodeEncodeError:
            print(text.encode("utf-8", errors="replace").decode("utf-8"))
    return text
