# 🧠 Reddit User Persona Generator (FastAPI + Together.ai)

This web application allows users to paste a Reddit user's comment page URL and generate a psychological persona based on their Reddit activity. It uses FastAPI for the backend, Jinja2 templates for the frontend, Reddit API (via PRAW) to fetch comments, and Together.ai's open-source LLMs (like Mistral) to analyze and generate the persona.

---

## 🚀 Features

- ✅ Validate and accept Reddit comment page URLs like:  
  `https://www.reddit.com/user/kojied/comments/`
- 📥 Scrapes recent Reddit comments for that user
- 🧠 Generates a detailed persona using Together.ai LLMs
- 📂 Displays and saves output in a `.txt` file with citations
- 🌐 Simple, responsive frontend using HTML + SimpleCSS

---

## 📁 Folder Structure

```
reddit_persona_app/
├── main.py                  # FastAPI backend
├── reddit_scraper.py        # Reddit comment fetcher using PRAW
├── persona_generator.py     # Persona builder using Together.ai
├── utils.py                 # Reddit URL validator
├── templates/
│   ├── base.html            # Base layout for all pages
│   ├── index.html           # Input form for Reddit URL
│   └── result.html          # Displays generated persona
├── outputs/                 # Saved .txt persona files
├── .env                     # API keys (excluded via .gitignore)
├── .gitignore
├── requirements.txt
└── README.md
```

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/reddit-persona-generator.git
cd reddit-persona-generator
```

### 2. Create and Activate Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate     # On macOS/Linux
# venv\Scripts\activate.bat  # On Windows
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔐 Environment Configuration

Create a `.env` file in the root directory and add your credentials:

```env
REDDIT_CLIENT_ID=your_reddit_client_id
REDDIT_CLIENT_SECRET=your_reddit_client_secret
REDDIT_USER_AGENT=reddit-persona-app
TOGETHER_API_KEY=your_together_api_key
```

---

## 🔑 How to Get API Keys

### Reddit API (PRAW)
1. Go to [https://www.reddit.com/prefs/apps](https://www.reddit.com/prefs/apps)
2. Click **"Create Another App"**
3. Set **App Type** to `script`
4. Name: `reddit-persona-app`
5. Redirect URI: `http://localhost:8000`
6. Submit and copy:
   - `personal use script` = your **REDDIT_CLIENT_ID**
   - `secret` = your **REDDIT_CLIENT_SECRET**

### Together.ai API
1. Go to [https://platform.together.xyz](https://platform.together.xyz)
2. Create an account and generate a new API key
3. Add it to your `.env` as `TOGETHER_API_KEY`

---

## 🧠 Run the Application

```bash
uvicorn main:app --reload
```

Then open your browser and go to:

```
http://127.0.0.1:8000
```

---

## 🧪 How to Use

1. Paste a Reddit comment URL like:
   ```
   https://www.reddit.com/user/kojied/comments/
   ```
2. Click **"Generate Persona"**
3. The app will:
   - Scrape recent Reddit comments
   - Analyze the text with a free LLM
   - Generate a detailed user persona
   - Show the result in-browser
   - Save it to `/outputs/<username>.txt`

---

## 📄 Example Output

```
Username: u/kojied

Age Range: 25–35  
Traits: Analytical, sarcastic, curious  
Hobbies: Anime, gaming, tech news  
Ideology: Libertarian leaning  
Writing Style: Informal, sharp, witty  

Citations:
- [Comment in r/technology]: "Reddit mods acting like cops again. Smh."
- [Comment in r/anime]: "Jujutsu Kaisen is peaking rn."
```

---

## 📦 Technologies Used

- [FastAPI](https://fastapi.tiangolo.com/) – Python web framework
- [PRAW](https://praw.readthedocs.io/) – Reddit API wrapper
- [Together.ai](https://platform.together.xyz) – Free LLM provider
- [Jinja2](https://jinja.palletsprojects.com/) – HTML templating
- [python-dotenv](https://pypi.org/project/python-dotenv/) – Secure API config

---

## 📦 Deployment Options

You can deploy this on:
- [Render.com](https://render.com/)
- [Replit](https://replit.com/)
- [Hugging Face Spaces](https://huggingface.co/spaces) (with Gradio or Streamlit frontend)

---

## 📄 .gitignore

Make sure `.env` and `outputs/` are excluded by your `.gitignore`:

```
.env
outputs/
__pycache__/
```

You can add a safe template for others by creating:

```
.env.example
```

---

## 🛡️ License

This project is open-sourced under the MIT License.  
Feel free to fork, remix, and enhance it for your own use!

---

## 🙌 Credits

- Reddit API via [PRAW](https://praw.readthedocs.io/)
- Free LLMs powered by [Together.ai](https://platform.together.xyz/)
- FastAPI for the modern API backend

---
