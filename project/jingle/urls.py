from django.urls import path
from . import views

urlpatterns = [
    path('', views.jingle_home,name='jingle-home'),
    path('results/', views.jingle_top_search,name='jingle-results'),
    path('song/', views.jingle_results,name='jingle-song'),


]