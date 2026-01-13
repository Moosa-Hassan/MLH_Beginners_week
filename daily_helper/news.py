from newsapi import NewsApiClient
from config import NEWS_API_KEY

news_api = NewsApiClient(api_key=NEWS_API_KEY)

def get_news():
    response = news_api.get_everything(
        q='technology cybersecurity',
        language='en',
        sort_by='publishedAt',
        page_size=5
    )
    # {'status': 'ok', 'totalResults': 30, 'articles': []} this is the json returned
    # print(response['articles'])
    return response['articles'][:5]

