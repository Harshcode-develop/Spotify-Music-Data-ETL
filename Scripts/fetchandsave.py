import spotipy
from spotipy.oauth2 import SpotifyOAuth
import json

def fetchandsave(client_id, client_secret, redirect_uri, scope):
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
        client_id=client_id,
        client_secret=client_secret,
        redirect_uri=redirect_uri,
        scope=scope
    ))

    all_artists = sp.current_user_followed_artists(limit=50, after=None)

    with open('followed_artists.json', 'a', encoding='utf-8') as file:
        artist_info = all_artists['artists']
        json.dump(artist_info, file, ensure_ascii=False)
        file.write('\n')

def main():
   client_id="<client-id>"
   client_secret="<secret-key>"
   redirect_uri="http://localhost:6060/callback"
   scope="user-follow-read"

   fetchandsave(client_id, client_secret, redirect_uri, scope)
   print("Done")

if __name__ == "__main__":
    main()