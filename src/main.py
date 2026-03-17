
import sys

from services.llm_service import run_prompt

if __name__ == "__main__":
    print("Welcome to the LLM API!")
    from dotenv import load_dotenv
    load_dotenv()
    # Usage: python src/main.py [prompt_file]
    prompt_file = sys.argv[1] if len(sys.argv) > 1 else "summarize.txt"
    run_prompt(prompt_file)
