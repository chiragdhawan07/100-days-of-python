from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth

date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0"
}

response = requests.get(f"https://www.billboard.com/charts/hot-100/{date}/", headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

song_tags = soup.select("li ul li h3")
song_names = [song.getText().strip() for song in song_tags]

print(f"Found {len(song_names)} songs from Billboard Hot 100 ({date})")

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id="YOUR_CLIENT_ID",
        client_secret="YOUR_CLIENT_SECRET",
        show_dialog=True,
        cache_path="token.txt"
    )
)

user_id = sp.current_user()["id"]
print(f"Logged in as {user_id}")

song_uris = []
year = date.split("-")[0]

for song in song_names:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} not found on Spotify, skipped.")

playlist = sp.user_playlist_create(
    user=user_id,
    name=f"{date} Billboard 100",
    public=False,
    description=f"Top 100 songs from Billboard Hot 100 on {date}"
)

sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)
print(f"Playlist '{playlist['name']}' created successfully with {len(song_uris)} songs.")
