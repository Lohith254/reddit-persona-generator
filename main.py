from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from utils import validate_reddit_url
from reddit_scraper import fetch_user_comments
from persona_generator import generate_persona
import os

app = FastAPI()
templates = Jinja2Templates(directory="templates")

OUTPUT_DIR = "outputs"
os.makedirs(OUTPUT_DIR, exist_ok=True)

@app.get("/", response_class=HTMLResponse)
def homepage(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/generate", response_class=HTMLResponse)
async def generate(request: Request, reddit_url: str = Form(...)):
    try:
        username = validate_reddit_url(reddit_url)
    except ValueError as e:
        return templates.TemplateResponse("index.html", {
            "request": request, "error": str(e)
        })

    comments = fetch_user_comments(username)
    if not comments:
        return templates.TemplateResponse("index.html", {
            "request": request, "error": f"No comments found for u/{username}"
        })

    persona_text = generate_persona(username, comments)

    output_path = os.path.join(OUTPUT_DIR, f"{username}.txt")
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(persona_text)

    return templates.TemplateResponse("result.html", {
        "request": request,
        "username": username,
        "persona": persona_text
    })