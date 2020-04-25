from spotipy.oauth2 import SpotifyClientCredentials
import sys
import spotipy
import os
import string
import json


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
		"spotify_id":"",
		"artist_additional_names":"",
		"release_date":"",
		"spotify_song_link":"",
		"genres":"",
		"popularity":"",
		"song_name_short":"",
		"errors":""
	}	
	
	#gets list of songs from spotify from the given song name
	API_results = sp.search(q='track:' + name, type='track')
	
	#makes sure at least one result is returned, if not creates error
	if len(API_results['tracks']['items']) == 0:
		spotifyDict["errors"] = "No Spotify Results"
		return spotifyDict
		
	#processes name input, removes content inside paranthesis, removes puncuation
	name = name.lower()
	start = name.find( '(' )
	tempName = ""
	if start != -1:
		tempName = tempName[0:start-1]
	name = name.translate(str.maketrans('','',string.punctuation))
	
	#this loop looks for the first song with an exact match of name, if no exact match is found, selects the most relevent song
	for i in API_results['tracks']['items']:
		tempName = i["name"].lower()
		start = tempName.find( '(' )
		if start != -1:
			tempName = tempName[0:start-1]
		tempName = tempName.translate(str.maketrans('','',string.punctuation))
		if name == tempName:
			spotifyDict["song_name_short"] = tempName
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
	spotifyDict["spotify_id"] = API_results["id"]
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
	
	
def spotify_top_search(name):
	
	#creates spotify object
	sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())

	spotifyDict = {}
	#creates dictionary for each top element, and the list that stores them
	top_search_list = []
	#gets results
	API_results = sp.search(q='track:' + name, type='track')
	#returns error if no results are shown
	if len(API_results['tracks']['items']) == 0:
		return top_search_list
		
	#processes name input, removes content inside paranthesis, removes puncuation
	name = name.lower()
	start = name.find( '(' )
	tempName = ""
	if start != -1:
		tempName = tempName[0:start-1]
	name = name.translate(str.maketrans('','',string.punctuation))
	
	tempInt = 0
	numList = []
	
	#adds the indexs of song with the exact name
	for i in API_results['tracks']['items']:
		tempName = i["name"].lower()
		start = tempName.find( '(' )
		if start != -1:
			tempName = tempName[0:start-1]
		tempName = tempName.translate(str.maketrans('','',string.punctuation))
		if name == tempName:
			numList.append(tempInt)
		tempInt += 1
	#adds rest f indexs to the list	
	tempInt = 0	
	for i in API_results['tracks']['items']:
		if numList.count(tempInt) == 0:
			numList.append(tempInt)
		tempInt += 1

	#goes through the list of numbers and retrieves data, then adds dictionaries to list
	for i in numList:
		top_search_dict = {}
		temp_results = API_results['tracks']['items'][i]
		top_search_dict["explicit"] = temp_results['explicit']
		top_search_dict["artist_name"] = temp_results["artists"][0]["name"]
		top_search_dict["song_name"] = temp_results["name"]
		top_search_dict["song_cover_url"] = temp_results["album"]["images"][0]["url"]
		top_search_dict["spotify_id"] = temp_results["id"]
		top_search_list.append(top_search_dict)

	return top_search_list
	
def return_song(spotify_id):
	sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())

	track = sp.track(spotify_id)

	spotifyDict = {
			"artist_name":"",
			"song_name":"",
			"album_name":"",
			"song_cover_url":"",
			"song_duration":"",
			"artist_additional_names":"",
			"release_date":"",
			"spotify_song_link":"",
			"genres":"",
			"song_name_short":"",
			"preview":"",
			"errors":""
		}
	
	spotifyDict["artist_name"] = track["artists"][0]["name"]
	spotifyDict["song_name"] = track["name"]
	spotifyDict["album_name"] = track["album"]["name"]
	spotifyDict["song_cover_url"] = track["album"]["images"][0]["url"]
	spotifyDict["preview"] = track["preview_url"]
	spotifyDict["popularity"] = track["popularity"]
	
	
	#converts the duration in ms to hours, mins, and secs
	duration = track["duration_ms"]
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
	spotifyDict["release_date"] = track["album"]["release_date"]
	spotifyDict["spotify_song_link"] = track["external_urls"]["spotify"]
		
	#this loop adds all the featured artists to dictionary in one string
	tempInt = 0
	for i in track["artists"]:
		if tempInt == 1:
			spotifyDict["artist_additional_names"] += i["name"]
		if tempInt > 1:
			spotifyDict["artist_additional_names"] += ", "
			spotifyDict["artist_additional_names"] += i["name"] 
		tempInt += 1
			
	album = sp.album(track["album"]["uri"])
	artist = sp.artist(track["artists"][0]["uri"])
		
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
		
	tempName = track["name"].lower()
	start = tempName.find( '(' )
	if start != -1:
		tempName = tempName[0:start-1]
	tempName = tempName.translate(str.maketrans('','',string.punctuation))
	spotifyDict["song_name_short"] = tempName
		
	#returns dictionary of details
	return spotifyDict

def get_top_fifty():
	sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())
	playlist = sp.playlist_tracks('spotify:playlist:37i9dQZEVXbMDoHDwVN2tF',fields = 'items.track.name',limit= 50, market="US")
	topfiftysongs = []

	for item in playlist['items']:
		topfiftysongs.append(item['track']['name'])
	

	
		

	
	return topfiftysongs
