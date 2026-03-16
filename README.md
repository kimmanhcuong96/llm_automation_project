# LLM Automation Project

Simple starter structure for prompt -> LLM -> response automation.

## Run

By default, the project runs in mock mode (no network) until you configure a real endpoint.

1) Optional: set `API_URL` to your LLM HTTP endpoint to use a real API.

PowerShell example:

```powershell
$env:API_URL="https://your-host/chat"
python src/main.py
```

## Run Without Any API (Mock)

```powershell
$env:MOCK_LLM="1"
python src/main.py
```
