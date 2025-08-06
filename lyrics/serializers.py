# lyrics/serializers.py
from rest_framework import serializers
from .models import Song, Lyrics

class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ['id', 'title', 'artist', 'album_art']

class LyricsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lyrics
        fields = ['id', 'song', 'lyrics']
