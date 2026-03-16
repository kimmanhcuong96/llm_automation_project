
from config.settings import API_URL, MOCK_LLM, TIMEOUT

def call_llm(prompt: str) -> str:
    if MOCK_LLM:
        # Keep it predictable so you can test the pipeline without any external API.
        preview = prompt.strip().replace("\r\n", "\n")
        preview = preview[:400]
        return f"[MOCK_LLM] Received prompt ({len(prompt)} chars):\n{preview}\n"

    # Import lazily so MOCK_LLM can run without installing requests.
    import requests

    payload = {"message": prompt}
    response = requests.post(API_URL, json=payload, timeout=TIMEOUT)
    response.raise_for_status()
    try:
        data = response.json()
    except ValueError as e:
        raise RuntimeError("LLM API did not return valid JSON.") from e
    return data.get("response", "")
