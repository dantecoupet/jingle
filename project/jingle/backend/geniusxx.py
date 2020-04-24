import requests
from bs4 import BeautifulSoup


def genius_results(song_title, artist_name):
	#dictionary of info being obtainted from genius
	geniusDict = {
		"lyrics":"",
		"genius_page_views":"",
		"genius_song_link":"",
		"errors":""
	}
	
	#defines what URLs used and genius access token
	base_url = 'https://api.genius.com'
	headers = {'Authorization': 'Bearer ' + 'WFnSZBMagahelhcV9nd7T-a0iGMLOn6kGMq9NUluw9DqsPwvzKyyBuN_bz4jRy4a'}
	search_url = base_url + '/search'
	data = {'q': song_title + ' ' + artist_name}
	response = requests.get(search_url, data=data, headers=headers)
	json = response.json()
	remote_song_info = None
	#cycles throught results to find song
	for hit in json['response']['hits']:
		if artist_name.lower() in hit['result']['primary_artist']['name'].lower():
			remote_song_info = hit
			if "pageviews" in remote_song_info['result']['stats']:
				geniusDict["genius_page_views"] = remote_song_info['result']['stats']['pageviews']
			break

	#takes URL of song and scrapes the webstite for the lyrics
	if remote_song_info:
		song_url = remote_song_info['result']['url']
		geniusDict["genius_song_link"] = song_url
		page = requests.get(song_url)
		html = BeautifulSoup(page.text, 'html.parser')
		geniusDict["lyrics"] = html.find('div', class_='lyrics').get_text()
	else:
		geniusDict["errors"] = "No Genius Results"
				
	return geniusDict
