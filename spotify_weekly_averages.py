import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd
import os

client_credentials_manager = SpotifyClientCredentials(client_id='45ba55617bf54841bcffd73357a1e4c6', client_secret='7e6ce2c0f78c48a894e2dd6d2f7d09d6')

sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

data_year = '2017'
filelist = os.listdir('data/' + data_year + '/')
available_params = ["duration_ms", "acousticness", "danceability", "energy", "instrumentalness", "liveness", "loudness", "speechiness", "valence", "tempo"]

for i in available_params:
    selected_param = i
    weekly_average_list = []
    for j in filelist:
        df = pd.read_csv('data/' + data_year + '/' + j, header=1)
        
        block_1 = df['URL'][0:50]
        block_2 = df['URL'][50:100]
        block_3 = df['URL'][100:150]
        block_4 = df['URL'][150:200]
        
        blocklist = [block_1,block_2,block_3,block_4]
    
        weekly_average = []
        
        for k in blocklist:
            audio_feature_search = sp.audio_features(k)
            for l in range(len(audio_feature_search)):
                weekly_average.append(audio_feature_search[l][selected_param])
        
        to_append = sum(weekly_average)/len(weekly_average)
        weekly_average_list.append(to_append)

    output_file = open('output/text/' + data_year + '/weekly_average_' + selected_param + '.txt','w')
    for m in weekly_average_list:
        output_file.write(str(m) + '\n')
    output_file.close()
