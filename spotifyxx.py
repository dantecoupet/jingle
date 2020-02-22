from spotipy.oauth2 import SpotifyClientCredentials
import sys
import spotipy
import os


''' shows the albums and tracks for a given artist.
'''

os.environ["SPOTIPY_CLIENT_ID"] = "0fba21663641452ca01057225b46097e"
os.environ["SPOTIPY_CLIENT_SECRET"] = "0e8f1eac53d54d51ab8621ecdfea378c"


def spotify_results(name):
	sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())
	
	tempInt = 0
	
	spotifyDict = {
		"artist_name":"",
		"song_name":"",
		"album_name":"",
		"song_cover_url":"",
		"song_duration":"",
		"artist_additional_names":"",
		"release_date":"",
		"spotify_song_link":"",
		"genres":""
	}	
	
	API_results = sp.search(q='track:' + name, type='track')
	API_results = API_results['tracks']['items'][0]

	
	spotifyDict["artist_name"] = API_results["artists"][0]["name"]
	spotifyDict["song_name"] = API_results["name"]
	spotifyDict["album_name"] = API_results["album"]["name"]
	spotifyDict["song_cover_url"] = API_results["album"]["images"][0]["url"]
	spotifyDict["song_duration"] = API_results["duration_ms"]
	spotifyDict["release_date"] = API_results["album"]["release_date"]
	spotifyDict["spotify_song_link"] = API_results["external_urls"]["spotify"]
	
	
	for i in API_results["artists"]:
		if tempInt == 1:
			spotifyDict["artist_additional_names"] += i["name"]
		if tempInt > 1:
			spotifyDict["artist_additional_names"] += ", "
			spotifyDict["artist_additional_names"] += i["name"] 
		tempInt += 1
		
	album = sp.album(API_results["album"]["uri"])
	artist = sp.artist(API_results["artists"][0]["uri"])
	genreList = []

	
	for i in album["genres"]:
		if genreList.count(i) == 0:
			genreList.append(i)
		
	for i in artist["genres"]:
		if genreList.count(i) == 0:
			genreList.append(i)
	
		


	return spotifyDict