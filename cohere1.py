import cohere 
from api import apikey_cohere

def ai_chat(prompt):
    co = cohere.Client(apikey_cohere)
    response = co.chat( 
      model='command',
      message=prompt,
      temperature=0.3,
      prompt_truncation='auto',
      citation_quality='accurate',
      connectors=[{"id": "web-search"}]
    ) 
    
    res = response.text

    return res