from django.shortcuts import render
from django.http import HttpResponse
from .backend import master_results

# Create your views here.

def jingle_home(request):    

    #calls master response function, plugging in song name as parameter
    spotifyDict = master_results.get_master("don't matter to me")
    
    #wraps dictionary for the HTML page
    context = {
        'song': spotifyDict
    }
    
    #calls HTML page and passes in wrapped response
    return render(request, 'jingle/index.html',context)