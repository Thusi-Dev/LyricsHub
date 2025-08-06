# lyrics/music_recognition.py
import requests
#import base64
import os

#def recognize_song(audio_data):
#    api_token = os.environ.get('AUDD_API_TOKEN')
#    url = 'https://api.audd.io/'
#    data = {
#        'api_token': api_token,
#        'method': 'recognize',
#        'buffer': base64.b64encode(audio_data).decode('utf-8'),
#        'return': 'apple_music,spotify'
#    }
#    response = requests.post(url, data=data)
#    return response.json()

class MusicRecognizer:
    def __init__(self):
        self.api_key = os.getenv('AUDIOTAG_API_TOKEN')
        self.endpoint = 'https://audiotag.info/api'

    def recognize_song(self, audio_file):
        try:
            payload = {
		'action': 'stat',
                'api_key': self.api_key
            }
            response = requests.post(self.endpoint, data=payload)
            response.raise_for_status()  # Raise an exception for bad status codes
            return response.json()
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")
        except requests.exceptions.ConnectionError as conn_err:
            print(f"Error connecting to the API: {conn_err}")
        except requests.exceptions.Timeout as time_err:
            print(f"Timeout error occurred: {time_err}")
        except requests.exceptions.RequestException as err:
            print(f"Something went wrong: {err}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
        return None

# Usage
#api_key = "YOUR_API_KEY_HERE"
#recognizer = MusicRecognizer(api_key)
#audio_file = "path/to/audio/sample.mp3"
#result = recognizer.recognize_song(audio_file)
#if result:
#    print(result)
#else:
#    print("Failed to recognize the song.")
