from . import spotifyxx


def get_master(name):
	spotifyResults = spotifyxx.spotify_results(name)
	
	return spotifyResults
	
	
	