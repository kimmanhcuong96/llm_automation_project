
from prompt.loader import load_prompt
from llm.client import call_llm
from response.writer import save_response

def run_prompt(prompt_file: str):
    prompt = load_prompt(prompt_file)
    response = call_llm(prompt)

    output_file = prompt_file.replace(".txt", "_response.txt")
    save_response(output_file, response)
