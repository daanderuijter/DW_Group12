import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import numpy as np
import pandas as pd

client_credentials_manager = SpotifyClientCredentials(client_id='CLIENTID', client_secret='CLIENTKEY')

sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

file = 'data/regional-us-daily-latest.csv'
df = pd.read_csv(file, header=1)
print(df['URL'][0:10])


name = df['Artist'][0]
artist_search = sp.search(q='artist:' + name, type='artist')

artist_popularity = artist_search['artists']['items'][0]['popularity']
print('{} has a popularity score of: {}'.format(df['Artist'][0], artist_popularity))