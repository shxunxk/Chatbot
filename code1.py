import pyttsx3
import datetime
import speech_recognition as sr

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[0].id)
engine.setProperty('voice',voices[1].id)

def barbara():
    r = sr.Recognizer()
    with sr.Microphone() as src:
        r.pause_threshold = 1
        audio = r.listen(src)
    try:
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        barbara()
    return query


def speak(text):
    engine.say(text)
    engine.runAndWait()

def lis():
    r = sr.Recognizer()
    with sr.Microphone() as src:
        r.pause_threshold = 1
        audio = r.listen(src)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"{query}\n")
        query = query.title()
        if(query == 'That Is All'):
            speak('The pleasure is all mine')
            return 'None'
    except Exception as e:
        print('Say that again...')
        lis()
    return query

def greeting():
    hour = int(datetime.datetime.now().hour)
    minute = int(datetime.datetime.now().minute)
    if(hour>=4 and hour <12):
        speak("Good Morning, Its Barbara here, I Hope you are having a good day")
    elif(hour == 12 and minute==0):
        speak("Good Day, Its Barbara here, I Hope you are having a good day")
    elif(hour<=16):
        speak("Good Afternoon, Its Barbara here, I Hope you are having a good day")
    else:
       speak("Good Evening, Its Barbara here, I Hope you are having a good day")

if __name__=="__main__":
    print("Waiting...")
    query = barbara()
    query = query.title()
    if(query == 'Hello Barbara'):
        greeting()
        query = lis()