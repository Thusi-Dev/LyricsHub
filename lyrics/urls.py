# lyrics/urls.py
from django.urls import path
from .views import SongList, LyricsList, MusicRecognitionView, index


urlpatterns = [
    path('songs/', SongList.as_view()),
    path('lyrics/', LyricsList.as_view()),
	path('recognize-music/',MusicRecognitionView.as_view()),
	path('', index, name='index'),
]
