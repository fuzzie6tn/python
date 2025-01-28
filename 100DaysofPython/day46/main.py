# # music time machine
# import requests
# import spotipy
# from spotipy.oauth2 import SpotifyOAuth
# from bs4 import BeautifulSoup
#
# sp = spotipy.Spotify(
#     auth_manager=SpotifyOAuth(
#         scope="playlist-modify-private",
#         redirect_uri="http://example.com",
#         client_id= "eac8ba826f714cf8869b12bfb5e01215",
#         client_secret="2ffac3396e1648738917634938e1b1f1",
#         show_dialog=True,
#         cache_path="token.txt"
#     )
# )
#
# user_id = sp.current_user()["id"]
# date = input("Which year do you want travel to? Type the date in this format YYYY-MM-DD: ")
# song_names= ["The list of song", "titles from your", "web scrape"]
#
# client_ID = "eac8ba826f714cf8869b12bfb5e01215"
# client_secret = "2ffac3396e1648738917634938e1b1f1"
#
# song_uris = []
# year = date.split("-")[0]
#
# for song in song_names:
#     result= sp.search(q=f"track :{song} : {year}", type="track")
#     print(result)
#     try:
#         uri = result["tracks"]["items"][0]["uri"]
#         song_uris.append(uri)
#     except IndexError:
#         print(f"{song} doesn't exist in Spotify. Skipped.")
#
# # scrape 100 song title on that date into a python list
# response = requests.get("https://www.billboard.com/charts/hot-100/" + date)
#
# soup = BeautifulSoup(response.text, "html.parser")
# songs_names_spans = soup.select("li ul li h3")
# songs_names = [song.getText.strip() for song in songs_names_spans]

from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Scraping Billboard 100
date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
response = requests.get("https://www.billboard.com/charts/hot-100/" + date)
soup = BeautifulSoup(response.text, 'html.parser')
song_names_spans = soup.select("li ul li h3")
song_names = [song.getText().strip() for song in song_names_spans]

#Spotify Authentication
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id="eac8ba826f714cf8869b12bfb5e01215",
        client_secret="2ffac3396e1648738917634938e1b1f1",
        show_dialog=True,
        cache_path="token.txt"
    )
)
user_id = sp.current_user()["id"]
print(user_id)

#Searching Spotify for songs by title
song_uris = []
year = date.split("-")[0]
for song in song_names:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

#Creating a new private playlist in Spotify
playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)
print(playlist)

#Adding songs found into the new playlist
sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)

