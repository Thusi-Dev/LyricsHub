# lyrics/music_recognition.py
import requests
import base64
import os

def recognize_song(audio_data):
    api_token = os.environ.get('AUDD_API_TOKEN')
    url = 'https://api.audd.io/'
    data = {
        'api_token': api_token,
        'method': 'recognize',
        'buffer': base64.b64encode(audio_data).decode('utf-8'),
        'return': 'apple_music,spotify'
    }
    response = requests.post(url, data=data)
    return response.json()
