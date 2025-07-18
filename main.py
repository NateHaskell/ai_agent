import sys
import os
import argparse
from google import genai
from google.genai import types
from dotenv import load_dotenv


def main():
    load_dotenv()

    parser = argparse.ArgumentParser(description="A script that demonstrates command line flags")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    parser.add_argument("prompt", help="The user prompt")


    args = parser.parse_args()

    user_prompt = args.prompt
    

    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key) 

    messages = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)]),
    ]

    response = client.models.generate_content(
        model="gemini-2.0-flash-001",
        contents=messages,
    )    

    if args.verbose:
        print(f"User prompt: {user_prompt}")
        print("Prompt tokens:", response.usage_metadata.prompt_token_count)
        print("Response tokens:", response.usage_metadata.candidates_token_count)

    
    print(response.text)
    

if __name__ == "__main__":
    main()
