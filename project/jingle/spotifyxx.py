from spotipy.oauth2 import SpotifyClientCredentials
import sys
import spotipy
import os

''' shows the albums and tracks for a given artist.
'''

os.environ["SPOTIPY_CLIENT_ID"] = "0fba21663641452ca01057225b46097e"
os.environ["SPOTIPY_CLIENT_SECRET"] = "0e8f1eac53d54d51ab8621ecdfea378c"

def get_artist(name):
	sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())
	results = sp.search(q='artist:' + name, type='artist')
	items = results['artists']['items']
	if len(items) > 0:
		return items[0]
	else:
		return None

def find_song(name):
	sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())
	results = sp.search(q='track:' + name, type='track')
	items = results['tracks']['items']
	if len(items) > 0:
		return items[0]
	else:
		return 'None'