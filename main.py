import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types


def main():
    load_dotenv()

    user_argument = sys.argv[1:]

    if not user_argument:
        print("Error! Expecting an argument after main.py: python main.py 'your argument here'")
        sys.exit(1)

    user_prompt = " ".join(user_argument)
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)


    user_prompt = " ".join(user_argument)

    messages = [
            types.Content(role="user", parts=[types.Part(text=user_prompt)])
            ]

    generate_content(client, messages)


def generate_content(client, messages):
    response = client.models.generate_content(model="gemini-2.0-flash-001", contents=messages)
    print(response.text)


if __name__ == "__main__":
    main()

