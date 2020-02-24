from spotipy.oauth2 import SpotifyClientCredentials
import sys
import spotipy
import os


''' shows the albums and tracks for a given artist.
'''
#keys used by the spotify API for authentication
os.environ["SPOTIPY_CLIENT_ID"] = "0fba21663641452ca01057225b46097e"
os.environ["SPOTIPY_CLIENT_SECRET"] = "0e8f1eac53d54d51ab8621ecdfea378c"


def spotify_results(name):
	#creates spotify object sp, used to call functions from spotify
	sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())
	tempInt = 0
	final = 1
	
	#dictions of all the desired info that will be returned
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
	
	#gets list of songs from spotify from the given song name
	API_results = sp.search(q='track:' + name, type='track')
	
	#this loop looks for the first song with an exact match of name, if no exact match is found, selects the most relevent song
	for i in API_results['tracks']['items']:
		tempName = i["name"].lower()
		start = tempName.find( '(' )
		if start != -1:
			tempName = tempName[0:start-1]
		if name.lower() == tempName:
			final = 0
			break
		tempInt += 1
	
	#selects song based on loop above	
	if final == 0:
		API_results = API_results['tracks']['items'][tempInt]
	else:
		API_results = API_results['tracks']['items'][0]

	#assigns info in the diction from the API results 
	spotifyDict["artist_name"] = API_results["artists"][0]["name"]
	spotifyDict["song_name"] = API_results["name"]
	spotifyDict["album_name"] = API_results["album"]["name"]
	spotifyDict["song_cover_url"] = API_results["album"]["images"][0]["url"]
	
	#converts the duration in ms to hours, mins, and secs
	duration = API_results["duration_ms"]
	seconds = minutes = hours = 0
	while duration > 1000:
		seconds += 1
		duration -= 1000
	while seconds > 60:
		minutes += 1
		seconds -= 60
	while minutes > 60:
		hours += 1
		minutes -= 60
	if hours > 1:
		spotifyDict["song_duration"] += str(hours) + " Hours "
	if hours == 1:
		spotifyDict["song_duration"] += str(hours) + " Hour "		
	if minutes > 1:
		spotifyDict["song_duration"] += str(minutes) + " Minutes "
	if minutes == 1:
		spotifyDict["song_duration"] += str(minutes) + " Minute "			
	if seconds > 1:
		spotifyDict["song_duration"] += str(seconds) + " Seconds "
	if seconds == 1:
		spotifyDict["song_duration"] += str(seconds) + " Second "
	
	#assigns more dictionary variables
	spotifyDict["release_date"] = API_results["album"]["release_date"]
	spotifyDict["spotify_song_link"] = API_results["external_urls"]["spotify"]
	
	#this loop adds all the featured artists to dictionary in one string
	tempInt = 0
	for i in API_results["artists"]:
		if tempInt == 1:
			spotifyDict["artist_additional_names"] += i["name"]
		if tempInt > 1:
			spotifyDict["artist_additional_names"] += ", "
			spotifyDict["artist_additional_names"] += i["name"] 
		tempInt += 1
		
	album = sp.album(API_results["album"]["uri"])
	artist = sp.artist(API_results["artists"][0]["uri"])
	
	#generates a list of genres based on the song genres and artist genres
	genreList = []
	tempInt = 0
	
	for i in album["genres"]:
		if genreList.count(i) == 0:
			genreList.append(i.capitalize())	
	for i in artist["genres"]:
		if genreList.count(i) == 0:
			genreList.append(i.capitalize())
	for i in genreList:
		if tempInt == 0:
			spotifyDict["genres"] += i
		else:
			spotifyDict["genres"] += ", "
			spotifyDict["genres"] += i
		tempInt += 1
	
	#returns dictionary of details
	return spotifyDict