from bs4 import BeautifulSoup
import requests
import os
from dotenv import load_dotenv, find_dotenv
import spotipy
from spotipy.oauth2 import SpotifyOAuth


user_date = input("Enter the year you want to travel back to? (YYYY-MM-DD) : ")
# user_date= "2015-08-12"

response = requests.get(f"https://www.billboard.com/charts/hot-100/{user_date}")
billboard_page = response.text
soup = BeautifulSoup(billboard_page, "html.parser")

songs = soup.select("li ul li h3")
songs_list = [ song.get_text().strip() for song in songs]
songs_list = songs_list[:10]
print(songs_list)

# Spotify Authentication

dotenv_path = find_dotenv()
load_dotenv(dotenv_path)

client_id = os.getenv("client_id")
client_secret = os.getenv("client_secret")


sp_oauth = SpotifyOAuth(
    scope="playlist-modify-private",
    redirect_uri="http://example.com",
    client_id=client_id,
    client_secret=client_secret,
    show_dialog=True,
    cache_path="token.txt",
    username="krizhnatester",
)

# Fetch the access token from the file
token_info = sp_oauth.get_cached_token()
access_token = token_info["access_token"]

# Now you can use the access_token as needed
sp = spotipy.Spotify(auth=access_token)
user_id = sp.current_user()["id"]

url_lists = []

playlist = sp.user_playlist_create(user=user_id, name=f"{user_date} Billboard 100", public=False)

for song in songs_list:
    query = song
    search_type = 'track'

    url = 'https://api.spotify.com/v1/search'

    headers = {
        'Authorization': f'Bearer {access_token}'
    }

    params = {
        'q': query,
        'type': search_type,
        'limit': 1,
    }

    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        results = response.json()
        items = results.get('tracks', {}).get('items', [])

        if items:
            first_track_uri = items[0]['uri']
            url_lists.append(first_track_uri)
        else:
            print("No tracks found in the search results.")
    else:
        print(f"Error: {response.status_code} - {response.text}")

sp.playlist_add_items(playlist_id=playlist["id"], items=url_lists)
print("Done")

