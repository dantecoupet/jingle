from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from . import spotifyxx, genius

from .forms import SongForm


#renders the home page and form
def home(request):

    #if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = SongForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            text = form.cleaned_data
            songInfo = spotifyxx.find_song(text['songTitle'])
            print(songInfo)

            track = songInfo['name']
            artist = songInfo['artists'][0]['name']
            img = songInfo['album']['images'][0]['url']
            albumName = songInfo['album']['name']
            duration = songInfo['duration_ms']
            duration = (duration/1000)/60
            preview = songInfo['preview_url']

            details = {
                "artist":artist,
                "track":track,
                "imgSrc":img,
                "album":albumName,
                "duration":duration,
                "preview":preview,
            }

            context = {
                'song': details,
            }
            return render(request,'jingle/song.html',context)

    # if a GET (or any other method) we'll create a blank form
    else:
        form = SongForm()

    args = {
        'form': form,
    }

    return render(request, 'jingle/home.html', args)

#this function 
def get_song(request):
    return render(request,'jingle/song.html')

# def get_song(request):
#     theName = request.POST
#     print(theName['songName'])
#     artistInfo = spotifyxx.get_artist(theName['songName'])
#     artistName = artistInfo['name']
#     artistImg = artistInfo['images'][2]['url']
#     image = artistImg

#     data = [
#         {'artName': artistName},
#         {'img': image},
#     ]
#     #if this is a POST request we need to process the form data
#     if request.method == 'POST':
#         # create a form instance and populate it with data from the request:
#         form = SongForm(request.POST)
#         # check whether it's valid:
#         # if form.is_valid():

#     # if a GET (or any other method) we'll create a blank form
#     else:
#         form = SongForm()

#     args = {
#         'form': form,
#         'data': data,
#     }

#     return render(request, 'jingle/song.html', args)