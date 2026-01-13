from news import get_news
from summarizer import summarize
from emailer import send_email

def main():
    print("NEWS SUMMARIZER")
    
    articles = get_news()
    
    email = "Daily Cybersecurity News Digest\n\n"
    
    for article in articles:
        summary = summarize(article['title'],article['description'])
        email += f"{article['title']}\n{summary}\n\n"
        
        print(summary)
        print("-"*50)
        
    send_email(
        subject="Daily News Digest",
        body=email,
        to_email="email to send to"
    )
    
    

if __name__ == "__main__":
    main()