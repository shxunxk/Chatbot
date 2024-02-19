import cohere 
from api import apikey_cohere

def ai_chat(query):
    co = cohere.Client(apikey_cohere)
    response = co.chat( 
      model='command',
      message=query,
      temperature=0.3,
      prompt_truncation='auto',
      citation_quality='accurate',
      connectors=[{"id": "web-search"}]
    ) 
    res = response.text
    return res