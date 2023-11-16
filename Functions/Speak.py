import pyttsx3

def Speak(text):
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice',voices[0].id)
    engine.setProperty('rate',170)
    print(f'\nA.I : {text}\n')
    engine.say(text)
    engine.runAndWait()