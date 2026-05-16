from fastapi import FastAPI
from openai import OpenAI
from dotenv import load_dotenv
import os
from supabase_client import supabase
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

    supabase.table("history").insert({
        "email": "demo@user.com",
        "prompt": prompt,
        "result": result
    }).execute()

    return {
        "result": result
    }

@app.get("/history")
def get_history():

    response = supabase.table("history") \
        .select("*") \
        .execute()

    return response.data