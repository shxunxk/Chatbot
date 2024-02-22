import speech_recognition as sr

def Listen():
    r = sr.Recognizer()
    with sr.Microphone() as src:
        print('Listening...')
        r.pause_threshold = 1
        audio = r.listen(src,0,3)
    try:
        print('Recognizing...')
        query = r.recognize_google(audio, language='en-in')
        query = str(query).lower()
        print(f"{query}\n")
        return query
    except Exception as e:
        print('Say that again...\n')
        return ('Say that again...').lower()