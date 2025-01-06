import requests
import json
from scrapper import get_website_content_and_clean

def format_content_with_ollama(content, instructions):
    url = "http://localhost:11434/api/generate"
    headers = {"Content-Type": "application/json"}
    data = {
        "model": "llama3",  
        "prompt": f"{instructions}\n\nContent:\n{content}",
        "stream": False 
    }
    response = requests.post(url, headers=headers, data=json.dumps(data))
    if response.status_code == 200:
        result = response.json()
        return result.get("response", "").strip()
    else:
        raise Exception(f"Error: {response.status_code} - {response.text}")
