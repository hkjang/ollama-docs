import json
from pathlib import Path
import requests
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Retrieve API key from environment variable
DIFY_API_KEY = os.getenv("DIFY_API_KEY")
DIFY_API_URL = os.getenv("DIFY_API_URL")
if not DIFY_API_KEY:
    raise ValueError("DIFY_API_KEY is not set in the .env file")
if not DIFY_API_URL:
    raise ValueError("DIFY_API_URL is not set in the .env file")

# Your existing code logic can go here
print(f"Loaded API Key: {DIFY_API_KEY[:4]}***")  # Masked key for security
print(f"Loaded API URL: {DIFY_API_URL}")  # Masked key for security

def translate_text(api_key=DIFY_API_KEY, user_id="mark-doc", inputs={'input_text': 'Hello, how are you?', 'target_language': 'es'}):
    url = DIFY_API_URL
    headers = {
      'Authorization': f'Bearer {api_key}',
      'Content-Type': 'application/json'
    }
    data = {
      'inputs': inputs,
      'response_mode': 'blocking',
      'user': user_id
    }
    response = requests.post(url, headers=headers, json=data)
    
    try:
        # Check if the response status code indicates success (200 OK)
        response.raise_for_status()
        # Attempt to decode the JSON response
        json_response = response.json()
        return json_response['data']['outputs']
    except requests.exceptions.HTTPError as http_err:
        # Handle HTTP errors (e.g., 404 Not Found, 401 Unauthorized)
        print(f'HTTP error occurred: {http_err}')
    except requests.exceptions.RequestException as req_err:
        # Handle other requests-related errors (e.g., connection errors)
        print(f'Request error occurred: {req_err}')
    except json.decoder.JSONDecodeError:
        # Handle JSON decode errors (e.g., empty response body)
        print('Failed to decode JSON response')
    
    # Return None or an appropriate value in case of error
    return None


def translate_markdown_files(input_folder, output_folder, target_language="korean"):
    input_folder = Path(input_folder)
    output_folder = Path(output_folder)

    for markdown_file in input_folder.rglob("*.md"):
        relative_path = markdown_file.relative_to(input_folder)
        output_file = output_folder / relative_path

        # Check if the file already exists in the target directory
        if output_file.exists():
            print(f"Skipping {markdown_file}, translated file already exists.")
            continue

        output_file.parent.mkdir(parents=True, exist_ok=True)

        with open(markdown_file, "r", encoding="utf-8") as f:
            content = f.read()
            print(f"Translating {markdown_file} to {target_language}")

        translated_content = translate_text(inputs={'input_text': content, 'target_language': target_language})

        # Inside the loop, after translating the content
        if translated_content is not None:
            translated_text = translated_content['final']
            with open(output_file, "w", encoding="utf-8") as f:
                f.write(translated_text)
        else:
            print(f"Warning: No translated content for {markdown_file}. Skipping file.")

    print(f"Translation completed. Translated files are saved in {output_folder}")

# Example usage
translate_markdown_files("en", "ko", target_language="korean")