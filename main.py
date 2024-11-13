# main.py
from fastapi import FastAPI
import os
import requests

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "Welcome to Simple Chatbot"}

@app.post("/chat")
async def chat_with_bot(prompt: str):
    api_key = os.getenv("ANTHROPIC_API_KEY")
    headers = {"Authorization": f"Bearer {api_key}"}
    # Mock endpoint for testing - replace with the real Anthropic endpoint if available
    response = requests.post(
        "https://api.anthropic.com/v1/messages", 
        headers=headers, 
        json={"prompt": prompt, "model": "claude-v1"}
    )
    return response.json()
