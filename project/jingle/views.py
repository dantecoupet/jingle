from django.shortcuts import render
from django.http import HttpResponse
from .backend import master_results
from .forms import SearchForm

# Create your views here.

def jingle_home(request):
    return render(request, 'jingle/home.html')


def jingle_results(request):    

    #calls master response function, plugging in song name as parameter
    
    spotifyDict = master_results.get_master("enemies")
    
    #wraps dictionary for the HTML page
    context = {
        'song': spotifyDict
    }
    
    #calls HTML page and passes in wrapped response
    return render(request, 'jingle/results.html',context)
    
def jingle_top_search(request):
    
    results_list = master_results.get_top_search("enemies")
    
    context = {
        'songs': results_list
    }
    return render(request, 'jingle/top_results.html',context)
