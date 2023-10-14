from Barbara import speak_save, process, speak
from googleapiclient.discovery import build
from api import apikey_music
import pygame
from pytube import YouTube
from pydub import AudioSegment

pygame.mixer.init()

youtube = build(
    'youtube', 'v3', developerKey=apikey_music
)

def stream_audio(video_url, song_name):
    try:
        yt = YouTube(video_url)
        audio_stream = yt.streams.filter(only_audio=True).first()

        audio_data = audio_stream.stream_to_buffer()
        audio = AudioSegment.from_file(audio_data)

        pygame.mixer.music.load(audio.export(format="mp3", codec="mp3").decode())
        speak(f"Playing {song_name} from Youtube Music")
        pygame.mixer.music.play()

        pygame.time.wait(10000)

        pygame.mixer.music.stop()

    except Exception as e:
        print(f"Error streaming audio: {e}")


def sing_song(song_name):
    search_response = youtube.search().list(
    q=song_name,
    type='video',
    part='id',
    maxResults=1
    ).execute()

    video_id = search_response['items'][0]['id']['videoId']

    video_url = f'https://www.youtube.com/watch?v={video_id}'

    stream_audio(video_url, song_name)
    process()