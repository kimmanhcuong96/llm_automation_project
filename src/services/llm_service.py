
from prompt.loader import load_prompt
from llm.client import call_llm
from response.writer import save_response

def run_prompt(prompt_file: str):
    prompt = load_prompt(prompt_file)
    response = call_llm(prompt)

    # Save under responses/ using the input file's basename.
    stem = prompt_file.rsplit("\\", 1)[-1].rsplit("/", 1)[-1]
    if stem.lower().endswith(".txt"):
        output_file = stem[:-4] + "_response.txt"
    else:
        output_file = stem + "_response.txt"
    save_response(output_file, response)
