# 🤖 Reddit Persona Generator

This tool generates a detailed **user persona** from a Reddit user's public posts and comments using the Reddit API and Google Gemini (LLM). It scrapes the data, builds a structured prompt, and outputs a personality profile with quotes.

---

## 🚀 Features

- ✅ Scrapes Reddit comments and posts using Reddit API (PRAW)
- 🤖 Uses Google Gemini (1.5 Flash) to generate a persona
- ✨ Toggle between **Concise** (short summary) and **Detailed** (in-depth) modes
- 🎨 Streamlit frontend for real-time persona generation
- 📄 Outputs clean `.md` file, downloadable from UI
- 📂 Modular backend using FastAPI

---

## 📦 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/reddit-persona-generator.git
cd reddit-persona-generator
```

### 2. Create a Virtual Environment (optional but recommended)

```bash
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```
### 4. Run Frontend

```bash
streamlit run frontend/app.py
```
---

## 🔐 Setup `.env`

Create a `.env` file in the root directory with your Reddit & Gemini API credentials:

```env
REDDIT_CLIENT_ID=your_client_id
REDDIT_CLIENT_SECRET=your_client_secret
REDDIT_USER_AGENT=reddit-persona-scraper by u/your_username
GEMINI_API_KEY=your_gemini_api_key
```

---

## ⚙️ Usage

From the `reddit-persona-generator` folder, run the main script:

```bash
python main.py
```

You'll be prompted to enter a Reddit username or profile URL:

```
🔗 Enter Reddit profile URL or username: https://www.reddit.com/user/kojied/
```

The script will:
- Fetch up to 50 posts and 50 comments
- Use Gemini to generate a persona
- Save the output to `output/kojied_persona.txt`

---

## 🗂 Example Output

```
Name: Redditor u/kojied
Age Group: 25–35
Personality: Reflective, empathetic
Interests: Anime, mental health, philosophy
Goals: Improve social confidence
Quote: "I've been working on building healthier routines lately."
```

---

## 📁 Project Structure

```
reddit-persona-generator/
├── src/
│   ├── main.py                 # FastAPI backend entry point
│   └── utils/                  # Core backend logic
│       ├── reddit_scraper.py
│       ├── prompt_builder.py
│       ├── llm_connector.py
│       ├── io_utils.py
│       └── helpers.py
├── frontend/
│   └── app.py                  # Streamlit UI
├── output/                     # Generated persona files (optional)
├── .env                        # API keys (not pushed to GitHub)
├── requirements.txt
└── README.md
```

---

## 📌 Requirements

- Python 3.8+
- Reddit developer account with app credentials
- Google Gemini API key

---
