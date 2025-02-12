import requests
import json
from scrapper import get_website_content_and_clean
import openai

OPENAI_API_KEY = "your-openai-api-key-here"

def format_content_with_ollama(content, instructions):
    url = "http://localhost:11434/api/generate"
    headers = {"Content-Type": "application/json"}
    
    data = {
        "model": "mistral",  
        "prompt": f"You've been given the HTML of a scraped webpage, follow these instructions for what and how you need to output them: {instructions}\n\nHere is the extracted content:\n{content}\n\nReturn the output exactly as requested above.",
        "stream": False 
    }

    print("\n🧠 Sending to AI:", json.dumps(data, indent=2))  

    response = requests.post(url, headers=headers, data=json.dumps(data))
    
    if response.status_code == 200:
        result = response.json()
        print("\n🤖 AI Response:", result)  
        return result.get("response", "").strip()
    else:
        print("\n🚨 AI ERROR:", response.text)
        raise Exception(f"Error: {response.status_code} - {response.text}")
    
def format_content_with_openai(content, instructions):
    openai.api_key = OPENAI_API_KEY

    prompt = f"Follow these instructions: {instructions}\n\nHere is the extracted content:\n{content}"

    try:
        print("\n🧠 Sending to OpenAI:", prompt)
        response = openai.ChatCompletion.create(
            model="gpt-4-turbo",
            messages=[
                {"role": "system", "content": "You are a structured data extractor."},
                {"role": "user", "content": prompt}
            ]
        )
        result = response["choices"][0]["message"]["content"]
        print("\n🤖 OpenAI Response:", result)
        return result.strip()
    
    except Exception as e:
        print("\n🚨 OpenAI ERROR:", str(e))
        raise Exception(f"OpenAI Error: {str(e)}")
