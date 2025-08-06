from django.shortcuts import render

# Create your views here.
# lyrics/views.py
from rest_framework import generics
from .models import Song, Lyrics
from .serializers import SongSerializer, LyricsSerializer

class SongList(generics.ListCreateAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer

class LyricsList(generics.ListCreateAPIView):
    queryset = Lyrics.objects.all()
    serializer_class = LyricsSerializer

from rest_framework.response import Response
from rest_framework.views import APIView
from .music_recognition import recognize_song
#Minimalistic display
#class MusicRecognitionView(APIView):
#    def post(self, request):
#        audio_data = request.data['audio_data']
#        result = recognize_song(audio_data)

from .lyrics_fetcher import fetch_lyrics

class MusicRecognitionView(APIView):
    def post(self, request):
        audio_data = request.data['audio_data']
        result = recognize_song(audio_data)
        if 'result' in result and result['result']:
            song_metadata = {
                'title': result['result']['title'],
                'artist': result['result']['artist'],
                'album': result['result'].get('album', ''),
            }
            song, created = Song.objects.get_or_create(
                title=song_metadata['title'],
                artist=song_metadata['artist'],
                defaults={'album': song_metadata['album']},
            )
            lyrics = fetch_lyrics(song_metadata['title'], song_metadata['artist'])
            if lyrics:
                Lyrics.objects.get_or_create(song=song, lyrics=lyrics)
            return Response(song_metadata)
        else:
            return Response({'error': 'Song not recognized'}, status=400)

class LyricsView(APIView):
    def get(self, request, song_id):
        song = Song.objects.get(id=song_id)
        lyrics = Lyrics.objects.get(song=song)
        return Response({'lyrics': lyrics.lyrics})

class SongView(APIView):
    def get(self, request, song_id):
        song = Song.objects.get(id=song_id)
        # Return the song URL or audio data
        return Response({'url': song.url})
        
from django.http import HttpResponse

def index(request):
    return HttpResponse("Welcome to the Lyrics Hub!")