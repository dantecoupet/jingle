from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from . import spotifyxx, genius

# Create your views here.

name = "mac miller"
songtitle = "circles"

artistInfo = spotifyxx.get_artist(name)
artistName = artistInfo['name']
artistImg = artistInfo['images'][2]['url']
image = artistImg

lyric = genius.get_song_info(songtitle,name)
print(lyric)
info  = genius.scrap_song_url(lyric)
print(info)

posts = [
    {'artistName': artistName},
    {'img': image},
    {'info': info}
]

def home(request):
    context = {
        'posts': posts
    }
    return render(request,'jingle/home.html',context)

def get_song(request):
    return render(request, 'jingle/song.html')

