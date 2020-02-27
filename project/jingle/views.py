from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from . import spotifyxx, genius

from .forms import SongForm

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
    #if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = SongForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            text = form.cleaned_data
            return HttpResponseRedirect('jingle/song.html')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = SongForm()

    args = {
        'text': text,
        'form': form,
    }

    return render(request, 'jingle/song.html')