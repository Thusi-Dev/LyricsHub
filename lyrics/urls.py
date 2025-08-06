# lyrics/urls.py
from django.urls import path
from .views import SongList, LyricsList, MusicRecognitionView, index, SongView, LyricsView


urlpatterns = [
    path('songs/', SongList.as_view()),
    path('lyrics/', LyricsList.as_view()),
    path('recognize-music/',MusicRecognitionView.as_view()),
    path('', index, name='index'),
    path('songs/<int:song_id>/', SongView.as_view()),
    path('songs/<int:song_id>/lyrics/', LyricsView.as_view()),
]
