'''
Loops through all collected data for a given year, and exports a dataframe containing the explicit song count and mean rank
'''
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd
import os

# Credentials can also be managed locally by editing the client_id and client_secret in spotipy.oauth2.py
client_credentials_manager = SpotifyClientCredentials(client_id='45ba55617bf54841bcffd73357a1e4c6', client_secret='7e6ce2c0f78c48a894e2dd6d2f7d09d6')
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

data_years = ['2017','2018']
for year in data_years:
    filelist = os.listdir('data/' + year + '/')
    
    # Initialize the dataframe
    mycolumns = ['file','count','mean_rank']
    df = pd.DataFrame(columns=mycolumns)
    
    for i in filelist:
        
        df2 = pd.read_csv('data/' + year + '/' + i, header=1)
        explicit_list = [] 
        
        block_1 = df2['URL'][0:50]
        block_2 = df2['URL'][50:100]
        block_3 = df2['URL'][100:150]
        block_4 = df2['URL'][150:200]
        blocklist = [block_1,block_2,block_3,block_4] # Spotipy supports requests in batches up to 50 songs
        
        for j in blocklist:
            audio_feature_search = sp.tracks(j)
            
            for k in audio_feature_search['tracks']:
                 explicit_list.append(k['explicit'])
    
        df3 = pd.DataFrame()
        df3['rank']  = list(range(1,201))
        df3['explicit'] = explicit_list
    
        row = [i,
               df3.groupby('explicit')['rank'].count()[1],
               df3.groupby('explicit')['rank'].mean()[1]]
        
        df.loc[len(df)+1] = row
        
    df.to_csv(path_or_buf='output/dataframes/' + year + '/explicit.csv')
