'''
Loops through all collected data for a given year, and exports a dataframe containing the weekly averages
--takes about a minute to run--
'''
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd
import os

# Credentials can also be managed locally by editing the client_id and client_secret in spotipy.oauth2.py
client_credentials_manager = SpotifyClientCredentials(client_id='45ba55617bf54841bcffd73357a1e4c6', client_secret='7e6ce2c0f78c48a894e2dd6d2f7d09d6')
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

# List of all audio features that can be requested from the Spotify Web API
available_params = ["duration_ms", "acousticness", "danceability", "energy", "instrumentalness", "liveness", "loudness", "speechiness", "valence", "tempo"]

data_years = ['2017','2018']
for year in data_years:
    filelist = os.listdir('data/' + year + '/')
    
    for i in available_params[0:1]:
        
        selected_param = i
        mycolumns = ['file',selected_param]
        df = pd.DataFrame(columns=mycolumns)
        
        for j in filelist:
            
            df2 = pd.read_csv('data/' + year + '/' + j, header=1)
            weekly_average = []
            
            block_1 = df2['URL'][0:50]
            block_2 = df2['URL'][50:100]
            block_3 = df2['URL'][100:150]
            block_4 = df2['URL'][150:200]
            blocklist = [block_1,block_2,block_3,block_4] # Spotipy supports requests in batches up to 50 songs
            
            for k in blocklist:
                audio_feature_search = sp.audio_features(k)
                
                for l in range(len(audio_feature_search)):
                    weekly_average.append(audio_feature_search[l][selected_param])
            
            row = [j,sum(weekly_average)/len(weekly_average)]
            df.loc[len(df)+1] = row
    
        df.to_csv(path_or_buf='output/dataframes/' + year + '/' + selected_param + '.csv')
