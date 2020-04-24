from django.urls import path
from . import views

urlpatterns = [
    path('', views.jingle_home,name='jingle-home'),
    path('results/<slug:song>/', views.jingle_top_search,name='jingle-results'),
    path('song/<slug:spotify_id>/', views.jingle_results,name='jingle-song'),
    path('feedback/', views.jingle_feedback,name='jingle-feedback'),
    path('top_results/', views.jingle_topfifty,name='jingle-topfifty'),
    path('about/', views.about_page,name='jingle-about'),
    #path('topfifty/<slug:song>/', views.jingle_results,name='jingle-results'),
    #path('error', views.jinge_error,name='jingle-error'),
]