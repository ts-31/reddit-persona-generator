# src/main.py (FastAPI backend)
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from utils.reddit_scraper import fetch_user_data
from utils.prompt_builder import build_prompt
from utils.llm_connector import generate_persona
from utils.helpers import extract_username

app = FastAPI()

# Allow CORS for frontend testing
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class RedditRequest(BaseModel):
    url: str

@app.post("/generate-persona")
async def generate_persona_api(payload: RedditRequest):
    username = extract_username(payload.url)
    print(f"\n🚀 Generating persona for u/{username} via API")

    posts, comments = fetch_user_data(username, save_to_file=False)
    if not posts and not comments:
        return {"error": "No Reddit data found for this user."}

    prompt = build_prompt(username, posts, comments)
    persona = generate_persona(prompt)

    return {
        "username": username,
        "persona": persona
    }
