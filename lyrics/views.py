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

#from .music_recognition import recognize_song
#Minimalistic display
#class MusicRecognitionView(APIView):
#    def post(self, request):
#        audio_data = request.data['audio_data']
#        result = recognize_song(audio_data)

from .lyrics_fetcher import fetch_lyrics

'''class MusicRecognitionView(APIView):
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

'''

from .music_recognition import MusicRecognizer
class MusicRecognitionView(APIView):
    def post(self, request):
        recognizer = MusicRecognizer()

        audio_file = request.FILES.get('audio_file')
        if not audio_file:
            return Response({'error': 'No audio file provided'}, status=400)

        result = recognizer.recognize_song(audio_file)
        if result:
            song_title = result.get('title')
            song_artist = result.get('artist')

            song, created = Song.objects.get_or_create(title=song_title, artist=song_artist)

            lyrics_obj, lyrics_created = Lyrics.objects.get_or_create(song=song)
            if lyrics_created:
                lyrics_obj.lyrics = fetch_lyrics(song_title, song_artist)
                lyrics_obj.save()

            return Response({
                'result': {
                    'full_title': f'{song_title} by {song_artist}',
                    'title': song_title,
                    'artist': song_artist,
                    'lyrics': lyrics_obj.lyrics,
                }
            })
        else:
            return Response({'error': 'Failed to recognize song'}, status=500)


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
