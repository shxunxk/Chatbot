import pyttsx3
import datetime
import speech_recognition as sr

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[0].id)
engine.setProperty('voice',voices[1].id)
# engine.say("Yuvaan piso")
# engine.runAndWait()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def lis():
    r = sr.Recognizer()
    with sr.Microphone() as src:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(src)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        print('Say that again...')
        return 'None'
    return query

def greeting():
    hour = int(datetime.datetime.now().hour)
    minute = int(datetime.datetime.now().minute)
    if(hour>=4 and hour <12):
        speak("Good Morning")
    elif(hour == 12 and minute==0):
        speak("Good Day")
    else:
        speak("Wank off")
if __name__=="__main__":
    # greeting()
    lis()