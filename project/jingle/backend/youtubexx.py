import requests

def get_youtube(song, artist):
	search_params = {
		'part': 'snippet',
		'q': song + ' ' + artist,
		'key': 'AIzaSyD-ALkXytH1CKrsYSyzTSVTzt8c3PeazM4',
		'maxResults': 3,
		'type': 'video'
	}

	#get information from youtube api
	video_ids = []
	videos = []
	search_url = 'https://www.googleapis.com/youtube/v3/search'
	video_url = 'https://www.googleapis.com/youtube/v3/videos'
	vid = requests.get(search_url, params=search_params)
	results_v = vid.json()['items']

	for result in results_v:
		video_ids.append(result['id']['videoId'])

	video_params = {
		'key': 'AIzaSyD-ALkXytH1CKrsYSyzTSVTzt8c3PeazM4',
		'part': 'snippet, contentDetails',
		'id': ','.join(video_ids)
	}

	vid2 = requests.get(video_url, params=video_params)

	results_t = vid2.json()['items']

	for result in results_t:
		video_data = {
			'title': result['snippet']['title'],
			'id': result['id'],
			'url': f'https://www.youtube.com/watch?v={result["id"]}',
			'thumbnail': result['snippet']['thumbnails']['high']['url']
			}

		videos.append(video_data)
		
	return videos

