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
        urlRedirect = urlRedirect.replace(" ","-")
        return HttpResponseRedirect(urlRedirect)
    
    return render(request,'jingle/home.html')


def jingle_results(request,spotify_id):    

    #calls master response function, plugging in song name as parameter
        
    spotifyDict = master_results.get_master(spotify_id)
    
    #wraps dictionary for the HTML page
    context = {
        'song': spotifyDict
    }
    
    #calls HTML page and passes in wrapped response
    return render(request, 'jingle/results.html',context)
    
def jingle_top_search(request,song):
    
    song = song.replace('-',' ')
    
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
        urlRedirect = urlRedirect.replace(" ","-")
        return HttpResponseRedirect(urlRedirect)
        
    return render(request, 'jingle/top_results.html',context)
