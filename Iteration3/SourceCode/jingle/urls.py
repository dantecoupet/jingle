from django.urls import path
from . import views

urlpatterns = [
    path('', views.jingle_home,name='jingle-home'),
    path('results/<str:song>/', views.jingle_top_search,name='jingle-results'),
    path('song/<slug:spotify_id>/', views.jingle_results,name='jingle-song'),
    path('feedback/', views.jinge_feedback,name='jingle-feedback'),
    path('topfifty/', views.jinge_topfifty,name='jingle-topfifty'),
    #path('topfifty/<slug:song>/', views.jingle_results,name='jingle-results'),
    #path('error', views.jinge_error,name='jingle-error'),
]
