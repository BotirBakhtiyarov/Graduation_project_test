import openai
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_summary(text: str) -> str:
    messages = [
        {"role": "system", "content": "You are an assistant that summarizes scientific literature."},
        {"role": "user", "content": f"Please provide a concise summary of the following scientific literature:\n\n{text}\n\nSummary:"}
    ]
    try:
        response = openai.chat.completions.create(
            model="gpt-4o-mini",  # or "gpt-4"
            messages=messages,
            max_tokens=500,
            temperature=0.7,
        )
        summary = response.choices[0].message.content.strip().strip()
        return summary
    except Exception as e:
        return f"Error generating summary: {e}"

def generate_outline(text: str) -> str:
    messages = [
        {"role": "system", "content": "You are an assistant that summarizes scientific literature."},
        {"role": "user", "content": f"Analyze the following scientific literature and provide a structured outline with main sections such as Introduction, Methods, Results, and Discussion:\n\n{text}\n\nOutline:"}
    ]
    try:
        response = openai.chat.completions.create(
            model="gpt-4o-mini",  # or "gpt-4"
            messages=messages,
            max_tokens=500,
            temperature=0.7,
        )
        outline = response.choices[0].message.content.strip()
        return outline
    except Exception as e:
        return f"Error generating outline: {e}"
