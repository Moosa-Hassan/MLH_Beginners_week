from dotenv import load_dotenv
import os

load_dotenv()

NEWS_API_KEY = os.getenv("NEWS_API_KEY") 
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
EMAIL_USER = os.getenv("EMAIL_USER")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")