from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

posts = [
    {'songName': 'yummy'},
    {'songName': 'the box'},
    {'songName': 'mo bamba'},
    {'songName': 'sicko mode'}
]

def jingle_home(request):
    context = {
        'posts': posts
    }
    return render(request, 'jingle/index.html', context)