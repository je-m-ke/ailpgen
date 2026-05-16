from fastapi import FastAPI
from openai import OpenAI
from dotenv import load_dotenv
import os

from database import conn, cursor

load_dotenv()

app = FastAPI()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

@app.get("/")
def home():
    return {"message": "API is working"}

@app.get("/generate")
def generate(prompt: str, style: str):

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {
                "role": "user",
                "content": f"""
You are an expert SaaS copywriter.

Create modern landing page copy.

Startup idea:
{prompt}

Landing page style:
{style}

Output format:

# Hero Title

# Subtitle

# Features

# Call To Action

Keep it clean, modern, and startup-style.
"""
            }
        ]
    )

    result = response.choices[0].message.content

    cursor.execute(
        "INSERT INTO history (prompt, result) VALUES (?, ?)",
        (prompt, result)
    )

    conn.commit()

    return {
        "result": result
    }

@app.get("/history")
def get_history():

    cursor.execute(
        "SELECT prompt, result FROM history ORDER BY id DESC"
    )

    rows = cursor.fetchall()

    history = []

    for row in rows:
        history.append({
            "prompt": row[0],
            "result": row[1]
        })

    return history