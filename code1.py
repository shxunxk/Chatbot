import pyttsx3
import datetime
import speech_recognition as sr
import webbrowser
import os
from datetime import datetime
from cohere1 import ai_chat
from newsapi import news_api

# Properties and function

name = 'Barbara'
born_on = (datetime.strptime('26 Sep 2023',"%d %b %Y"))
created_by = 'Shaunak Nagvenkar'
creator_socials = []
creator_info = [['hometown','Panaji, Goa, India'], ['studies', 'Bachelors of Technology in Computer Science Engineering', 'Vellore Institute of Technology, Vellore, Tamil Nadu, India']]
current_date = datetime.now()

if (current_date.month, current_date.day) < (born_on.month, born_on.day):
    age = current_date.year - born_on.year - 1
else:
    age = current_date.year - born_on.year

def name_details(query):
    if('What' in query):
        speak('My name is barbara, I am a chatbot created by Shuanak Nagvenkar')
    elif('change' in query):
        speak('What wouuld you prefer to call me?')
        query = lis()
        global name
        name = query
        speak(f'Okay, {name} it is then...')

def build_details(query):
    if(('you' in query or 'your' in query) and not 'age' in query ):
        speak(f'I was built on {born_on} by {created_by}')

def creator_details():
    speak(f'I was built by {created_by}, he is based in {creator_info[0][1]} and is pursuing {creator_info[1][1]} degree from {creator_info[1][2]}')



# voice intitalise

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[0].id)
engine.setProperty('voice',voices[1].id)



# barbara functions

def barbara():
    r = sr.Recognizer()
    with sr.Microphone() as src:
        r.pause_threshold = 1
        audio = r.listen(src)
    try:
        query = r.recognize_google(audio, language='en-in')
        query = query.title()
        print(f"{query}\n")
        return query
    except Exception as e:
        barbara()



# speak function

def speak(text):
    engine.say(text)
    engine.runAndWait()



# listen function

def lis():
    r = sr.Recognizer()
    with sr.Microphone() as src:
        r.pause_threshold = 1
        audio = r.listen(src)
    try:
        query = r.recognize_google(audio, language='en-in')
        query = query.capitalize()
        print(f"{query}\n")
        if('that is all' in query or 'bye' in query or 'thank you' in query or 'that is it' in query or 'I am done' in query):
            speak('The pleasure is all mine')
            return 'None'
        return query
    except Exception as e:
        print('Say that again...')
        return ''
    


# greeting function

def greeting():
    hour = int(datetime.now().hour)
    minute = int(datetime.now().minute)
    if(hour>=4 and hour <12):
        speak("Good Morning, Its Barbara here, I Hope you are having a good day")
    elif(hour == 12 and minute==0):
        speak("Good Day, Its Barbara here, I Hope you are having a good day")
    elif(hour<=16):
        speak("Good Afternoon, Its Barbara here, I Hope you are having a good day")
    else:
       speak("Good Evening, Its Barbara here, I Hope you are having a good day")


#speak & save 
def speak_save(res, query):
    text = f'{query}\n{res}'
    try:
        speak(res)
        if not os.path.exists("Cohere1"):
            os.mkdir('Cohere1')
        with open(f'Cohere1/{query[0:20]}.txt','w') as f:
                f.write(text)
    except Exception as e:
            speak('Error occured')



# API's


# chat function api

def chat(query):
    res = ai_chat(query)
    speak_save(res, query)
    

# news function api

def news(query):
    res=news_api(query)
    speak_save(res, query)


# driver function

def process():
    query = lis()
    if('open a website' in query or 'search a website' in query or 'search on the web' in query):
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
    elif('your name' in query or 'you called' in query):
        name_details(query)
        process()
    elif('birthday' in query or 'created' in query or 'built' in query):
        build_details()
        process()
    elif('created you' in query or 'built you' in query or 'your parents' in query):
        creator_details()
        process()
    elif('news' in query or 'latest news' in query):
        news(query)
    else:
        chat(query)
        process()



# main 

if __name__=="__main__":
    while True:
        print("Waiting...")
        query = barbara()
        if(query == 'Hello Barbara'):
            greeting()
            process()