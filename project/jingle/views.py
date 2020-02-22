from django.shortcuts import render
from django.http import HttpResponse
from . import master_results

# Create your views here.

def jingle_home(request):    

    spotifyDict = master_results.get_master("Hot shower")
    print(spotifyDict["artist_name"])
    
    context = {
        'song': spotifyDict
    }

    return render(request, 'jingle/index.html',context)