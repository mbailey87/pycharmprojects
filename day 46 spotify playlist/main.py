import requests, os
from bs4 import BeautifulSoup
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyOAuth, SpotifyClientCredentials
import pprint

load_dotenv()

date = '2017-12-16' #input("Input a date in YYYY-MM-DD format\n")
url = f"https://www.billboard.com/charts/hot-100/{date}"
header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0"}



response = requests.get(url=url, headers=header)

soup = BeautifulSoup(response.text, 'html.parser')

chart_list = soup.find(class_='chart-results-list')

songs = chart_list.select('.c-title.a-no-trucate')

artists = chart_list.select('.c-label.a-no-trucate')

artists_list = [artist.getText().replace('\t', '').replace('\n', '') for artist in artists]


song_list = [song.getText().replace('\t', '').replace('\n', '') for song in songs]

track_list = [[song, artist] for song, artist in zip(song_list, artists_list)]

print(track_list)

client_id = os.getenv('CLIENT_ID')
client_secret = os.getenv('CLIENT_SECRET')

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id,
                                               client_secret=client_secret,
                                               redirect_uri="http://example.com",
                                               scope="playlist-modify-private",
                                               username='31casqb35cbk5r5bjtwnzwz55csa',
                                               cache_path='token.txt',
                                               show_dialog=True,

                                               )
                     )

user = sp.current_user()['id']

song_uris = []
year = date.split("-")[0]

for song in song_list:
    result = sp.search(q=f"track:{song} year:{year}", type="track")

    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

print(song_uris)
playlist_name =f'{date} Billboard 100'
playlist = sp.user_playlist_create(user=user, name=playlist_name, public=False)
sp.user_playlist_add_tracks(user=user, playlist_id=playlist['id'], tracks=song_uris)



