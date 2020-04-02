import requests
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .backend import master_results
from .forms import SearchForm
from django.views import View
from django.views.generic.edit import FormView
from django.utils.dateformat import format


# Create your views here.

def jingle_home(request):
    template_name = 'home.html'
    form_class = SearchForm

    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            song = form.cleaned_data.get('song')
        else:
            song = "blank"
        urlRedirect = "/results/" + song + "/"
        urlRedirect = urlRedirect.replace(" ", "-")
        return HttpResponseRedirect(urlRedirect)

    return render(request, 'jingle/home.html')


def jingle_results(request, spotify_id):
    # calls master response function, plugging in song name as parameter

    spotifyDict = master_results.get_master(spotify_id)

    search_params = {
        'part': 'snippet',
        'q': spotifyDict['song_name'],
        'key': 'AIzaSyD-ALkXytH1CKrsYSyzTSVTzt8c3PeazM4',
        'maxResults': 3,
        'type': 'video'
    }

    # get information from youtube api
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

    # wraps dictionary for the HTML page
    context = {
        'song': spotifyDict,
        'videos': videos
    }

    # calls HTML page and passes in wrapped response
    return render(request, 'jingle/results.html', context)


def jingle_top_search(request, song):
    song = song.replace('-', ' ')

    results_list = master_results.get_top_search(song)

    context = {
        'songs': results_list
    }

    if request.method == 'POST':
        form = ResultsForm(request.POST)
        if form.is_valid():
            spotify_id = form.cleaned_data.get('spotify_id')
        else:
            spotify_id = "blank"
        urlRedirect = "/song/" + spotify_id + "/"
        urlRedirect = urlRedirect.replace(" ", "-")
        return HttpResponseRedirect(urlRedirect)

    return render(request, 'jingle/top_results.html', context)
