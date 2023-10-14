from api import apikey_news
import requests
from Barbara import speak_save

def newsapi(query):
    url = (f'https://newsapi.org/v2/top-headlines?q=trump&apiKey={apikey_news}')

    response = requests.get(url)
    res = response.json()
    speak_save(res, query)