import os

from config.settings import API_URL, LLM_PROVIDER, MODEL_NAME, MOCK_LLM, TIMEOUT


def _response_to_text(resp) -> str:
    # Prefer SDK convenience attribute if available.
    output_text = getattr(resp, "output_text", None)
    if isinstance(output_text, str) and output_text.strip():
        return output_text.strip()

    # Fallback: extract text from the structured "output" items.
    output = getattr(resp, "output", None)
    if isinstance(resp, dict) and output is None:
        output = resp.get("output")

    parts: list[str] = []
    if isinstance(output, list):
        for item in output:
            item_type = getattr(item, "type", None)
            if isinstance(item, dict) and item_type is None:
                item_type = item.get("type")

            if item_type != "message":
                continue

            content = getattr(item, "content", None)
            if isinstance(item, dict) and content is None:
                content = item.get("content")

            if not isinstance(content, list):
                continue

            for c in content:
                c_type = getattr(c, "type", None)
                if isinstance(c, dict) and c_type is None:
                    c_type = c.get("type")

                if c_type in {"output_text", "text"}:
                    text = getattr(c, "text", None)
                    if isinstance(c, dict) and text is None:
                        text = c.get("text")
                    if isinstance(text, str) and text:
                        parts.append(text)

    return "\n".join(p.strip() for p in parts if p.strip()).strip()


def call_llm(prompt: str) -> str:
    provider = LLM_PROVIDER
    if not provider:
        # Heuristic default to preserve the starter-template behavior.
        provider = "mock" if MOCK_LLM else "http"
    if provider == "mock":
        print("running mock LLM")
        # Keep it predictable so you can test the pipeline without any external API.
        preview = prompt.strip().replace("\r\n", "\n")
        preview = preview[:400]
        return f"[MOCK_LLM] Received prompt ({len(prompt)} chars):\n{preview}\n"

    if provider == "openai":
        # Import lazily so "mock"/"http" can run without installing openai.
        from openai import OpenAI
        print("running openai LLM")
        client = OpenAI()  # Uses env var OPENAI_API_KEY by default.
        resp = client.responses.create(
            model=MODEL_NAME,
            input=prompt,
        )
        return _response_to_text(resp)

    if provider == "groq":
        # Groq exposes an OpenAI-compatible API; use the same OpenAI SDK with a custom base_url.
        from openai import OpenAI
        print("running groq LLM")
        api_key = os.getenv("GROQ_API_KEY")
        if not api_key:
            raise RuntimeError(
                "LLM_PROVIDER=groq requires GROQ_API_KEY to be set (env var or .env)."
            )

        base_url = os.getenv("GROQ_BASE_URL", "https://api.groq.com/openai/v1")
        client = OpenAI(api_key=api_key, base_url=base_url)
        resp = client.responses.create(
            model=MODEL_NAME,
            input=prompt,
        )
        print(resp.usage)
        return _response_to_text(resp)

    if provider != "http":
        print("running not http LLM")
        raise ValueError(
            f"Unsupported LLM_PROVIDER={LLM_PROVIDER!r}. Expected: mock|openai|groq|http."
        )

    # Import lazily so "mock" can run without installing requests.
    import requests

    payload = {"message": prompt}
    response = requests.post(API_URL, json=payload, timeout=TIMEOUT)
    response.raise_for_status()
    try:
        data = response.json()
    except ValueError as e:
        raise RuntimeError("LLM API did not return valid JSON.") from e
    return data.get("response", "")
