from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,name='home'),
    path('', views.get_song,name='song'),
]