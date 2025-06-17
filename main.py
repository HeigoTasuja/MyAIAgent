import os
import sys
import argparse
from dotenv import load_dotenv

from google import genai
from google.genai import types
from google.genai.types import GenerateContentResponseUsageMetadataOrDict


def main():
    load_dotenv()

    user_argument = sys.argv[1:]
    parser = argparse.ArgumentParser()
    parser.add_argument('prompt', type=str, help="Question or propmt to the AI agent")
    parser.add_argument('--verbose', action='store_true')
    args = parser.parse_args()

    if not user_argument:
        print("Error! Expecting an argument after main.py: python main.py 'your argument here'")
        sys.exit(1)

    user_prompt = " ".join(user_argument)
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)

    user_prompt = " ".join(user_argument)

    generate_content(client, user_prompt, args.verbose)

def generate_content(client, user_prompt, verbose=False):
    messages = [types.Content(role="user", parts=[types.Part(text=user_prompt)])]
    response = client.models.generate_content(model="gemini-2.0-flash-001", contents=messages)
    if verbose:
        prompt_tokens = response.usage_metadata.prompt_token_count
        response_tokens = response.usage_metadata.candidates_token_count
        print(f"User prompt: {user_prompt}")
        print(f"Prompt tokens: {prompt_tokens}")
        print(f"Response tokens: {response_tokens}")
    print(response.text)


if __name__ == '__main__':
    main()

