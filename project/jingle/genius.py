import requests
from bs4 import BeautifulSoup

#wonderful human that explained the code
#https://dev.to/willamesoares/how-to-integrate-spotify-and-genius-api-to-easily-crawl-song-lyrics-with-python-4o62
def get_song_info(song_title, artist_name):
    base_url = 'https://api.genius.com'
    headers = {'Authorization': 'Bearer ' + 'WFnSZBMagahelhcV9nd7T-a0iGMLOn6kGMq9NUluw9DqsPwvzKyyBuN_bz4jRy4a'}
    search_url = base_url + '/search'
    data = {'q': song_title + ' ' + artist_name}
    response = requests.get(search_url, data=data, headers=headers)

    json = response.json()
    remote_song_info = None
    for hit in json['response']['hits']:
        if artist_name.lower() in hit['result']['primary_artist']['name'].lower():
            remote_song_info = hit
            break

    if remote_song_info:
        song_url = remote_song_info['result']['url']

    return song_url

def scrap_song_url(url):
    page = requests.get(url)
    html = BeautifulSoup(page.text, 'html.parser')
    lyrics = html.find('div', class_='lyrics').get_text()

    return lyrics