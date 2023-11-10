# from gtts import gTTS
# import pyttsx3
# from datetime import datetime
# import os
# import webbrowser
# from cohere1 import ai_chat
# from newsapi import newsapi
# from googleapiclient.discovery import build
# import pygame
# from pytube import YouTube
# from pydub import AudioSegment
# import subprocess
# from api import apikey_music
# import requests
# from api import api_weather

# # Properties and function

# name = 'Barbara'
# born_on = (datetime.strptime('26 Sep 2023',"%d %b %Y"))
# created_by = 'Shaunak Nagvenkar'
# creator_socials = []
# creator_info = [['hometown','Panaji, Goa, India'], ['studies', 'Bachelors of Technology in Computer Science Engineering', 'Vellore Institute of Technology, Vellore, Tamil Nadu, India']]
# current_date = datetime.now()

# if (current_date.month, current_date.day) < (born_on.month, born_on.day):
#     age = current_date.year - born_on.year - 1
# else:
#     age = current_date.year - born_on.year

# def name_details(query):
#     if('What' in query):
#         speak('My name is barbara, I am a chatbot created by Shuanak Nagvenkar')
#     elif('change' in query):
#         speak('What would you prefer to call me?')
#         query = lis()
#         global name
#         name = query
#         speak(f'Okay, {name} it is then...')
#     process()

# def build_details(query):
#     if(('you' in query or 'your' in query) and not 'age' in query ):
#         speak(f'I was built on {born_on} by {created_by}')
#     process()

# def creator_details():
#     speak(f'I was built by {created_by}, he is based in {creator_info[0][1]} and is pursuing {creator_info[1][1]} degree from {creator_info[1][2]}')
#     process()

# # voice intitalise



# # barbara functions

# def barbara():
#     r = sr.Recognizer()
#     with sr.Microphone() as src:
#         r.pause_threshold = 1
#         audio = r.listen(src)
#     try:
#         query = r.recognize_google(audio, language='en-in')
#         query = query.title()
#         print(f"{query}\n")
#         return query
#     except Exception as e:
#         barbara()

# # speak function


# # listen function


# # greeting function

# def greeting():
#     hour = int(datetime.now().hour)
#     minute = int(datetime.now().minute)
#     if(hour>=4 and hour <12):
#         speak("Good Morning, Its Barbara here, I Hope you are having a good day")
#     elif(hour == 12 and minute==0):
#         speak("Good Day, Its Barbara here, I Hope you are having a good day")
#     elif(hour<=16):
#         speak("Good Afternoon, Its Barbara here, I Hope you are having a good day")
#     else:
#        speak("Good Evening, Its Barbara here, I Hope you are having a good day")

# #speak & save

# def speak_save(res, query):
#     text = f'{query}\n{res}'
#     try:
#         speak(res)
#         if not os.path.exists("Cohere1"):
#             os.mkdir('Cohere1')
#         with open(f'Cohere1/{query[0:20]}.txt','w') as f:
#                 f.write(text)
#     except Exception as e:
#             speak('Error occured')

        
# def open_application(query):
#     speak("Which application do you want me to open?")
#     query = lis()
#     if(query != ""):
#         query = query.lower()
#         speak("On it")
#         subprocess.call(f'{query}.exe')
#     else:
#         lis()
#     process()


# def open_website(query):
#     speak("Which site do you want me to search for?")
#     query = lis()
#     if(query != ""):
#         query = query.lower()
#         speak("On it")
#         site = 'www.'+query+'.com'
#         webbrowser.open(site)
#     else:
#         lis()
#     process()


# # def sing_song(song_name):
    

# def sing():
#     speak("What song do you want to hear?")
#     song_name = lis()
#     try:
#         youtube = build('youtube', 'v3', developerKey=apikey_music)
#         search_response = youtube.search().list(
#             q=song_name,
#             type='video',
#             part='id',
#             maxResults=1
#         ).execute()
#         video_id = search_response['items'][0]['id']['videoId']
#         video_url = f'https://www.youtube.com/watch?v={video_id}'
#         yt = YouTube(video_url)
#         audio_stream = yt.streams.filter(only_audio=True).first()
#         audio_stream.download(filename='temp_audio.mp3')
#         pygame.mixer.init()
#         pygame.mixer.music.load('temp_audio.mp3')
#         speak(f"Playing {song_name} from Youtube Music")
#         pygame.mixer.music.play()
#         pygame.time.wait(1000)
#         pygame.mixer.music.stop()
#         os.remove('temp_audio.mp3')
#     except FileNotFoundError as e:
#         speak(f"File not found: {e}")
#     except pygame.error as e:
#         speak(f"Pygame error: {e}")
#     except Exception as e:
#         speak(f"Error playing song: {e}")
#         process()
#     pygame.mixer.init()


# def set_alarm(time, command):
#         try:
#             alarm_command = f'at {time}'
#             alarm_process = subprocess.Popen(alarm_command, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#             alarm_process.communicate(input=command.encode())

#             print(f'Alarm set for {time}.')
#         except Exception as e:
#             print(f'An error occurred: {e}')


# def weather():
#     if 'in' in query:
#         speak('Please specify the city name')
#         city_name = lis()
#     else:
#         city_name='Goa'
#         country_code='IN'
#     geo_url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name},{country_code}&appid={api_weather}"
#     resp = requests.get(geo_url)
#     if resp.status_code == 200:
#         data = resp.json()
#         print(data)
#         if 'coord' in data:
#             lat = data['coord']['lat']
#             lon = data['coord']['lon']
#             url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_weather}"
#             resp1 = requests.get(url)
#             if resp1.status_code == 200:
#                 data1 = resp1.json()
#                 if 'weather' in data1:
#                     speak(f"The weather in {city_name} is {data1['weather']['main']} with {data1['weather']['description']}.")
#                 else:
#                     speak("Weather data not found")
#             else:
#                 speak(f"Failed to retrieve weather data. Status code: {resp1.status_code}")
#         else:
#             speak("Weather data not found.")
#     else:
#         speak(f"Failed to retrieve weather data. Status code: {resp.status_code}")


# # driver function

# def process():
#     query = lis()
#     if('open a website' in query or 'search a website' in query or 'search on the web' in query):
#         open_website(query)

#     elif('open a application' in query or 'open a software' in query or 'open a program' in query):
#         open_application(query)

#     elif('your name' in query or 'you called' in query):
#         name_details(query)

#     elif('birthday' in query or 'created' in query or 'built' in query):
#         build_details(query)

#     elif('created you' in query or 'built you' in query or 'your parents' in query):
#         creator_details()

#     elif('alarm' in query):
#         if('delete' in query):
#             set_alarm(query)
#         else:
#             set_alarm(query)

#     elif('news' in query or 'latest news' in query):
#         newsapi(query)
#         speak_save(res, query)
#         process()

#     elif('play a song' in query):
#         sing()

#     elif('weather' in query):
#         weather(query)

#     else:
#         res = ai_chat(query)
#         speak_save(res, query)
#         process()

# # main 

# if __name__=="__main__":
#     while True:
#         print("Waiting...")
#         query = barbara()
#         if(query == 'Hello Barbara'):
#             greeting()
#             process()