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
            
            search_params = {
                'part': 'snippet',
                'q': track + ' ' + artist,
                'key': 'AIzaSyD-ALkXytH1CKrsYSyzTSVTzt8c3PeazM4',
                'maxResults': 3,
                'type': 'video'
            }

            #get information from youtube api
            video_ids = []
            videos = []
            search_url = 'https://www.googleapis.com/youtube/v3/search'
            video_url = 'https://www.googleapis.com/youtube/v3/videos'
            vid = requests.get(search_url, params=search_params)
            results_v = vid.json()['items']

            for result in results_v:
                video_ids.append(result['id']['videoId'])

            video_params = {
                'key': 'AIzaSyD-ALkXytH1CKrsYSyzTSVTzt8c3PeazM4',
                'part': 'snippet, contentDetails',
                'id': ','.join(video_ids)
            }

            vid2 = requests.get(video_url, params=video_params)

            results_t = vid2.json()['items']

            for result in results_t:
                video_data = {
                    'title': result['snippet']['title'],
                    'id': result['id'],
                    'url': f'https://www.youtube.com/watch?v={result["id"]}',
                    'thumbnail': result['snippet']['thumbnails']['high']['url']
                }

                videos.append(video_data)


            context = {
                'song': details,
                'form':form,
                'videos':videos
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
            
            search_params = {
                'part': 'snippet',
                'q': track + ' ' + artist,
                'key': 'AIzaSyD-ALkXytH1CKrsYSyzTSVTzt8c3PeazM4',
                'maxResults': 3,
                'type': 'video'
            }

            #get information from youtube api
            video_ids = []
            videos = []
            search_url = 'https://www.googleapis.com/youtube/v3/search'
            video_url = 'https://www.googleapis.com/youtube/v3/videos'
            vid = requests.get(search_url, params=search_params)
            results_v = vid.json()['items']

            for result in results_v:
                video_ids.append(result['id']['videoId'])

            video_params = {
                'key': 'AIzaSyD-ALkXytH1CKrsYSyzTSVTzt8c3PeazM4',
                'part': 'snippet, contentDetails',
                'id': ','.join(video_ids)
            }

            vid2 = requests.get(video_url, params=video_params)

            results_t = vid2.json()['items']

            for result in results_t:
                video_data = {
                    'title': result['snippet']['title'],
                    'id': result['id'],
                    'url': f'https://www.youtube.com/watch?v={result["id"]}',
                    'thumbnail': result['snippet']['thumbnails']['high']['url']
                }

                videos.append(video_data)


            context = {
                'song': details,
                'form':form,
                'videos', videos
            }

            #return render(request,'jingle/results.html',context)
            return render(request,'jingle/results.html',context)

    return render(request,'jingle/results.html')
