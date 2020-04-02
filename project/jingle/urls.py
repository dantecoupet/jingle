from django.urls import path
from . import views

urlpatterns = [
    path('', views.jingle_home,name='jingle-home'),
    path('results/<slug:song>/', views.jingle_top_search,name='jingle-results'),
    path('song/<slug:spotify_id>/', views.jingle_results,name='jingle-song'),
    path('feedback/', views.jinge_feedback,name='jingle-feedback'),
    #path('feedback/thanks/', views.jinge_thanks,name='jingle-thanks'),
    #path('about/', views.jinge_about,name='jingle-about'),
    #path('error', views.jinge_error,name='jingle-error'),
]