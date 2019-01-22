import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import numpy as np
import pandas as pd
import os

client_credentials_manager = SpotifyClientCredentials(client_id='45ba55617bf54841bcffd73357a1e4c6', client_secret='7e6ce2c0f78c48a894e2dd6d2f7d09d6')

sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

filelist = os.listdir('data/')

weekly_average_list = []

for i in filelist:
    df = pd.read_csv('data/' + i, header=1)
    
    block_1 = df['URL'][0:49]
    block_2 = df['URL'][50:99]
    block_3 = df['URL'][100:149]
    block_4 = df['URL'][150:199]
    
    blocklist = [block_1,block_2,block_3,block_4]

    weekly_average = []
    measured_param = "acousticness"
    
    for i in blocklist:
        audio_feature_search = sp.audio_features(i)
        for i in range(len(audio_feature_search)):
            weekly_average.append(audio_feature_search[i][measured_param])
    
    to_append = sum(weekly_average)/len(weekly_average)
    weekly_average_list.append(to_append)

print('A list of the weekly averages of the valence feature:{} '.format(weekly_average_list))

output_file = open('output/weekly_average_' + measured_param + '.txt','w')
output_file.write(str(weekly_average_list))
output_file.close() 

'''
print(df['URL'][0:10])

name = df['Artist'][0]
artist_search = sp.search(q='artist:' + name, type='artist')

artist_popularity = artist_search['artists']['items'][0]['popularity']
print('{} has a popularity score of: {}'.format(df['Artist'][0], artist_popularity))

audio_feature_search = sp.audio_features(df['URL'][0:2])
print(audio_feature_search[0]["valence"])
'''