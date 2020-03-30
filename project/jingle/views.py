import requests
from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpResponseRedirect
from . import spotifyxx, genius
from .forms import SongForm

def home(request):
    if request.method == 'POST':

        form = SongForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data['songTitle']
            form = SongForm()

            songInfo = spotifyxx.find_song(text)
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
                'form':form,
            }
            #return render(request,'jingle/results.html',context)
            return render(request,'jingle/results.html',context)
    else:
        form = SongForm()

    return render(request, 'jingle/home.html', {'form':form})

def results(request):
    if request.method == 'POST':

        form = SongForm(request.POST)
        if form.is_valid():
            song = form.cleaned_data['songTitle']
            form = SongForm()

            songInfo = spotifyxx.find_song(song)
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
                'form':form,
            }

            #return render(request,'jingle/results.html',context)
            return render(request,'jingle/results.html',context)

    return render(request,'jingle/results.html')
