from google import genai
from config import GEMINI_API_KEY


client = genai.Client(api_key=GEMINI_API_KEY)

def summarize(title, description):
    prompt = f"""
    Summarize this news in 3-5 bullet points.
    Use simple language.
    No opinions.

    Follow the format below for each article
    Title: {title}
    Description: {description}
    Summary in bullet points.
    """
    response = client.models.generate_content(
        model="models/gemini-2.5-flash",
        contents=prompt
    )
    return response.text