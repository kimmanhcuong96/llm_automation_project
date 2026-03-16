
import requests
from config.settings import API_URL

def call_llm(prompt: str) -> str:
    payload = {"message": prompt}
    response = requests.post(API_URL, json=payload)
    data = response.json()
    return data.get("response", "")
