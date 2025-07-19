import os
import requests
from dotenv import load_dotenv

load_dotenv()
TOGETHER_API_KEY = os.getenv("TOGETHER_API_KEY")
TOGETHER_MODEL = "mistralai/Mistral-7B-Instruct-v0.2"

def generate_prompt(username, comments):
    comment_text = "\n".join([f"[Comment in r/{c['subreddit']}]: {c['body'][:300]}" for c in comments])
    return f"""
You are a Reddit behavior analyst.

Build a detailed persona for Reddit user u/{username} based only on the comment history below.

Include:
- Age Range
- Personality Traits
- Hobbies and Interests
- Occupation Clues
- Political or Ideological Views
- Commenting Style and Tone

Cite excerpts from comments for each trait.

Reddit Comments:
{comment_text}
"""

def generate_persona(username, comments):
    prompt = generate_prompt(username, comments)
    url = "https://api.together.xyz/v1/chat/completions"

    headers = {
        "Authorization": f"Bearer {TOGETHER_API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": TOGETHER_MODEL,
        "messages": [
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.7
    }

    try:
        response = requests.post(url, headers=headers, json=payload)
        result = response.json()
        return result["choices"][0]["message"]["content"]
    except Exception as e:
        print("LLM Error:", e)
        return "Persona generation failed due to LLM error."