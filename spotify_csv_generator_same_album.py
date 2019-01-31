'''
Loops through all collected data for a given year, and exports a dataframe containing the amount of unique albums
'''
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd
import os

# Credentials can also be managed locally by editing the client_id and client_secret in spotipy.oauth2.py
client_credentials_manager = SpotifyClientCredentials(client_id='45ba55617bf54841bcffd73357a1e4c6', client_secret='7e6ce2c0f78c48a894e2dd6d2f7d09d6')
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

# Initialize the dataframe
mycolumns = ['file','unique_albums']
df1 = pd.DataFrame(columns=mycolumns)

data_years = ['2017','2018']

for year in data_years:
    filelist = os.listdir('data/' + year + '/')
    
    for i in filelist:
        df2 = pd.read_csv('data/' + year + '/' + i, header=1)
        album_list = []
        
        block_1 = df2['URL'][0:50]
        block_2 = df2['URL'][50:100]
        block_3 = df2['URL'][100:150]
        block_4 = df2['URL'][150:200]
        blocklist = [block_1,block_2,block_3,block_4] # Spotipy supports requests in batches up to 50 songs

        # If we only want the top n < 50
        '''
        n = 50
        block_1 = df2['URL'][0:n]
        blocklist = [block_1]
        '''
        
        for j in blocklist:
            audio_feature_search = sp.tracks(j)
            
            for k in audio_feature_search['tracks']:
                album_list.append(k['album']['name'])
        
        row = [i] + [len(set(album_list))] # set operation gets rid of duplicate entries
        df1.loc[len(df1)+1] = row
    
df1.to_csv(path_or_buf='output/dataframes/all/albums.csv')
#df1.to_csv(path_or_buf='output/dataframes/all/albums_top_' + str(n) + '.csv')
