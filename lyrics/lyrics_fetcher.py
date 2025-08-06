# lyrics/lyrics_fetcher.py
import requests
import os

def fetch_lyrics(song_title, artist):
    api_token = os.environ.get('GENIUS_API_TOKEN')
    url = f'https://api.genius.com/search?q={song_title} {artist}'
    headers = {'Authorization': f'Bearer {api_token}'}
    response = requests.get(url, headers=headers)
    data = response.json()
    if data['response']['hits']:
        song_id = data['response']['hits'][0]['result']['id']
        lyrics_url = f'https://api.genius.com/songs/{song_id}'
        response = requests.get(lyrics_url, headers=headers)
        data = response.json()
        lyrics = data['response']['song']['description']['dom']['children'][0]['children'][0]['string']
        return lyrics
    else:
        return None
