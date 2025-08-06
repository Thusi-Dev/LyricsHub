# lyrics/urls.py
from django.urls import path
from .views import SongList, LyricsList, MusicRecognitionView


urlpatterns = [
    path('songs/', SongList.as_view()),
    path('lyrics/', LyricsList.as_view()),
	path('recognize-music/',MusicRecognition.as_view()),
]
