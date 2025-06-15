import os
import sys
import argparse
from dotenv import load_dotenv
from google import genai
from google.genai import types
from call_function import call_function, available_functions 
from config import MAX_ITERS


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

    iters = 0
    while True: 
        iters += 1
        if iters > MAX_ITERS:
            print(f"Maximum iterations ({MAX_ITERS}) rached.")
            sys.exit(1)

        try:
            final_response = generate_content(client, messages, verbose)
            if final_response:
                print("Final response:")
                print(final_response)
                break
        except Exception as e:
            print(f"Error in generate_content: {e}")
        
   

def generate_content(client, messages, verbose):
    system_prompt = """
You are a helpful AI coding agent.

When a user asks a question or makes a request, your first action should always be to list all available files and directories by calling `get_files_info`. 

You can call the following operations:
- List files and directories
- Read file contents
- Execute Python files with optional arguments
- Write or Overwrite files

At every turn, prefer to call tools rather than ask the user for clarification unless absolutely necessary.

All paths you provide should be relative to the working directory. You do not need to specify the working directory in your function calls as it is automatically injected for security reasons.

When you have completed your task, summarize what you did in plain text as your final response.
"""

    response = client.models.generate_content(
        model='gemini-2.0-flash-001', 
        contents=messages,
        config=types.GenerateContentConfig(
            tools=[available_functions],
            system_instruction=system_prompt),
    )

    if verbose:
        prompt_tokens = response.usage_metadata.prompt_token_count
        response_tokens = response.usage_metadata.candidates_token_count
        print(f"Prompt tokens: {prompt_tokens}")
        print(f"Response tokens: {response_tokens}") 

    if response.candidates:
        for candidate in response.candidates:
            function_call_content = candidate.content
            messages.append(function_call_content)
    
    if not response.function_calls:
        return response.text 
    
    function_responses = []
    for call in response.function_calls:
        call_response = call_function(call, verbose)
        if (
            not call_response.parts
            or not call_response.parts[0].function_response
        ):
            raise Exception("empty function call results")
        if verbose:
            print(f"-> {call_response.parts[0].function_response.response}")
        function_responses.append(call_response.parts[0])
    
    if not function_responses:
        raise Exception("no function responses generated, exiting.")
    
    messages.append(types.Content(role="tool", parts=function_responses))
        

if __name__ == "__main__":
    main()