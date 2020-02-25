from . import spotifyxx
from . import geniusxx


#master dictionary that will be returned
masterDict = {
		#spotify API
		"artist_name":"",
		"song_name":"",
		"album_name":"",
		"song_cover_url":"",
		"song_duration":"",
		"artist_additional_names":"",
		"release_date":"",
		"spotify_song_link":"",
		"genres":"",
		#genius API
		"lyrics":"",
		"genius_page_views":"",
		"genius_song_link":"",
		"errors":""
	}


#master function that calls all the sub functions from other files
def get_master(name):
	
	#calls the spotify function and passes in name of song
	spotifyResults = spotifyxx.spotify_results(name)
	masterDict["artist_name"] = spotifyResults["artist_name"]
	masterDict["song_name"] = spotifyResults["song_name"]
	masterDict["album_name"] = spotifyResults["album_name"]
	masterDict["song_cover_url"] = spotifyResults["song_cover_url"]
	masterDict["song_duration"] = spotifyResults["song_duration"]
	masterDict["artist_additional_names"] = spotifyResults["artist_additional_names"]
	masterDict["release_date"] = spotifyResults["release_date"]
	masterDict["spotify_song_link"] = spotifyResults["spotify_song_link"]
	masterDict["genres"] = spotifyResults["genres"]
	masterDict["errors"] = spotifyResults["errors"]
	
	#calls the genius function, passing in song/artist name from spotify
	if masterDict["errors"] == "":
		geniusResults = geniusxx.genius_results(masterDict["song_name"], masterDict["artist_name"])
		masterDict["lyrics"] = geniusResults["lyrics"]
		masterDict["genius_page_views"] = geniusResults["genius_page_views"]
		masterDict["genius_song_link"] = geniusResults["genius_song_link"]
		masterDict["errors"] = geniusResults["errors"]

	return masterDict
	
	
	