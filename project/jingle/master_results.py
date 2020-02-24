from . import spotifyxx

#master function that calls all the sub functions from other files
def get_master(name):
	#calls the spotify function and passes in name of song
	spotifyResults = spotifyxx.spotify_results(name)
	
	return spotifyResults
	
	
	