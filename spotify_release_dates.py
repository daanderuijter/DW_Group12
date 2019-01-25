import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd
import os
from dateutil.parser import parse

def days_between(d1, d2):
    d1 = parse(d1)
    d2 = parse(d2)
    return abs((d2 - d1).days)

client_credentials_manager = SpotifyClientCredentials(client_id='45ba55617bf54841bcffd73357a1e4c6', client_secret='7e6ce2c0f78c48a894e2dd6d2f7d09d6')

sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

data_year = '2018'
filelist = os.listdir('data/' + data_year + '/')
mycolumns = ['file'] + list(range(1,201))
df = pd.DataFrame(columns=mycolumns)

for i in filelist:
    df2 = pd.read_csv('data/' + data_year + '/' + i, header=1)
    
    file_date = str(i[:-4].split('-')[-3] + '-' + i[:-4].split('-')[-2] + '-' + i[:-4].split('-')[-1])
    
    block_1 = df2['URL'][0:50]
    block_2 = df2['URL'][50:100]
    block_3 = df2['URL'][100:150]
    block_4 = df2['URL'][150:200]
    
    blocklist = [block_1,block_2,block_3,block_4]
    
    release_date_list = []
    
    for j in blocklist:
        audio_feature_search = sp.tracks(j)
        
        for k in audio_feature_search['tracks']:
             release_date_list.append(days_between(file_date, k['album']['release_date']))

    row = [i] + release_date_list
    
    df.loc[len(df)+1] = row
    
df.to_csv(path_or_buf='output/dataframes/' + data_year + '/release_date.csv')