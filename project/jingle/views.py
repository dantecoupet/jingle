from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from . import spotifyxx, genius

from .forms import SongForm

# Create your views here.

name = "mac miller"
songtitle = "circles"

temp = spotifyxx.find_song('the box')

lyric = genius.get_song_info(songtitle,name)
info  = genius.scrap_song_url(lyric)

posts = [
    # {'artistName': artistName},
    # {'img': image},
    # {'info': info}
]

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

            track = songInfo['name']
            artist = songInfo['artists']
            artistname = artist['external_urls']['name']
            print(artistname)
            allinfo = songInfo

            details = [
                {'track': track},
                {'artist': artist},
                {'all': allinfo},
            ]

            context = {
                'details': details,
            }
            return render(request,'jingle/song.html',context)

    # if a GET (or any other method) we'll create a blank form
    else:
        form = SongForm()

    args = {
        'form': form,
        'posts': posts,
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