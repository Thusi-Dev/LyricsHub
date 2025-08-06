from django.db import models

# Create your models here.
# lyrics/models.py
class Song(models.Model):
    title = models.CharField(max_length=255)
    artist = models.CharField(max_length=255)
    album = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f'{self.title} by {self.artist}'

class Lyrics(models.Model):
    song = models.ForeignKey(Song, on_delete=models.CASCADE)
    lyrics = models.TextField()
    
    def __str__(self):
        return f'Lyrics for {self.song.title}, by {self.song.artist}'
