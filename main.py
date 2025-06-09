import os
import sys
import argparse
from dotenv import load_dotenv
from google import genai
from google.genai import types


def main():
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)
    parser = argparse.ArgumentParser(description="Send your questions to Google GenAi")
    parser.add_argument("-v", "--verbose", action="store_true", help="Enable verbose output")
    parser.add_argument("user_prompt", help="Your prompt to GenAi")

    args = parser.parse_args()

    if not args: 
        print("AI Code Assistant")
        print('\nUsage: python main.py "your prompt here"')
        print('Example: python main.py "How do I build a calculator app?')
        sys.exit(1)
    user_prompt = " ".join(args.user_prompt)
    verbose = args.verbose

    if verbose:
          print(f"User prompt: {user_prompt}")

    messages = [
     types.Content(role="user", parts=[types.Part(text=user_prompt)]),
    ]

    generate_content(client, messages, verbose)

def generate_content(client, messages, verbose):
    response = client.models.generate_content(
        model='gemini-2.0-flash-001', 
        contents=messages,
    )
    print(response.text)

    if verbose:
        prompt_tokens = response.usage_metadata.prompt_token_count
        response_tokens = response.usage_metadata.candidates_token_count
        print(f"Prompt tokens: {prompt_tokens}")
        print(f"Response tokens: {response_tokens}") 

if __name__ == "__main__":
    main()