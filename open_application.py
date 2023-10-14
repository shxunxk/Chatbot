import os
from Barbara import speak, lis, process

def open_application(query):
    speak("Which application do you want me to open?")
    query = lis()
    if(query != ""):
        query = query.lower()
        speak("On it")
        os.system(f'{query}.exe')
    else:
        lis()
    process()