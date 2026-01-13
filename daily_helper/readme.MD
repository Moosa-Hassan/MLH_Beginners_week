# AI Daily News Helper

A Python-based daily assistant that fetches real-time news
and summarizes it using Google Gemini.

## Features
- Source-specific news (BBC, CNN, Verge)
- AI-generated summaries
- Sends Email

## Tech Stack
- Python
- NewsAPI
- Google Gemini

## How to Run
1. Clone repo
2. Add API keys to .env
3. pip install -r requirements.txt
4. python app.py


## Where to generate API KEYS
1. [NEWS API](https://newsapi.org/)
2. [Gemeni API](https://aistudio.google.com/api-keys)
3. Generate app password from google account

Set up .env file as below (dont put quotes)
1. NEWS_API_KEY=_api_key_from_newsapi
2. GEMINI_API_KEY=api_key_from_gemeni
3. EMAIL_USER=your_email
4. EMAIL_PASSWORD=16_char_password_without_spaces

