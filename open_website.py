import webbrowser
from Barbara import speak, lis, process

def open_website(query):
    speak("Which site do you want me to search for?")
    query = lis()
    if(query != ""):
        query = query.lower()
        speak("On it")
        site = 'www.'+query+'.com'
        webbrowser.open(site)
    else:
        lis()
    process()
