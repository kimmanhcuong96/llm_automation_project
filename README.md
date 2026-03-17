# LLM Automation Project

Simple starter structure for prompt -> LLM -> response automation.

## Run

By default, the project runs in mock mode (no network) until you configure a real endpoint.

Install deps:

```powershell
python -m pip install -e .
```

### Option A: OpenAI (recommended)

PowerShell example:

```powershell
$env:LLM_PROVIDER="openai"
$env:OPENAI_API_KEY="YOUR_KEY"
$env:MODEL_NAME="gpt-4.1-mini"
python src/main.py prompts/summarize.txt
```

### Option B: Groq (often cheaper/faster, still may have usage limits/cost)

```powershell
$env:LLM_PROVIDER="groq"
$env:GROQ_API_KEY="YOUR_KEY"
$env:MODEL_NAME="llama-3.1-8b-instant"
python src/main.py prompts/summarize.txt
```

Or create a `.env` file at the project root (see `.env.example`) and just run:

```powershell
python src/main.py prompts/summarize.txt
```

### Option C: Custom HTTP API

Set `API_URL` to your LLM HTTP endpoint to use a real API.

PowerShell example:

```powershell
$env:LLM_PROVIDER="http"
$env:API_URL="https://your-host/chat"
python src/main.py
```

## Run Without Any API (Mock)

```powershell
$env:MOCK_LLM="1"
python src/main.py
```
