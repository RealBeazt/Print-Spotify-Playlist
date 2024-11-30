from dotenv import load_dotenv
import requests
import base64
import os

load_dotenv()

client_id = os.getenv('CLIENT_ID')
client_secret = os.getenv('CLIENT_SECRET')

client_encoded = f'{client_id}:{client_secret}'
client_encoded = base64.b64encode(client_encoded.encode())

token_url = 'https://accounts.spotify.com/api/token'
token_data = {'grant_type': 'client_credentials'}
token_header = {"Authorization": f"Basic {client_encoded.decode()}"}

response = requests.post(token_url,data=token_data, headers=token_header)

# print(response)

response_info = response.json()

access_token = response_info['access_token']

playlist_id = os.getenv('PLAYLIST_ID')

playlist_url = f'https://api.spotify.com/v1/playlists/{playlist_id}'
playlist_url_header = {'Authorization': f'Bearer {access_token}'}

playlist_response = requests.get(playlist_url,headers=playlist_url_header)

# print(playlist_response)

playlist_response_info = playlist_response.json()

tracks = playlist_response_info['tracks']['items']

# print(tracks[0]['track']['artists'][0]['name'])

for id, item in enumerate(tracks):
    track = item['track']
    print(f"{id + 1}) {track['name']} by {', '.join(artist['name'] for artist in track['artists'])}")


