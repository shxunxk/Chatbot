from api import apikey_news
import requests

def news_api(query):
    url = (f'https://newsapi.org/v2/top-headlines?q=trump&apiKey={apikey_news}')

    response = requests.get(url)
    res = response.json()
    return response.articles.title