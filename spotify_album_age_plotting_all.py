'''
Loads the dataframes containing the weekly album age values for a given year and plots the averages by weeks and ranks
'''
import matplotlib.pyplot as plt
import pandas as pd

def get_album_age_df(df):
    album_df = pd.DataFrame(columns=list(range(1,201)))
    
    for i in range(0,52,4): #Groups 52 weeks into 13 groups of 4 weeks
        row = list(df.iloc[i:i+4].mean())
        album_df.loc[len(album_df)+1] = row
    
    return album_df.transpose().mean() # flips weeks and rank before averaging 

def get_track_age_df(df):
    track_df = pd.DataFrame(columns=['mean age'])

    for i in range(1,200,10): #Groups Top 200 into 20 groups of 10 tracks
        '''
        df.loc[:,str(i):str(i+9)]) = 10 rank columns * 52 week rows
        df.loc[:,str(i):str(i+9)].mean() = 1 week column * 10 rank rows
        df.loc[:,str(i):str(i+9)].mean().mean() = single float value
        '''
        row = df.loc[:,str(i):str(i+9)].mean().mean()
        track_df.loc[i] = row
    
    return track_df

data_years = ['2017','2018']

fig = plt.figure()

ax1 = fig.add_subplot(121, title = 'Average Age Of Albums', xlabel = 'Group of 4 weeks', ylabel = 'Album Age (days)')
df1 = get_album_age_df(pd.read_csv('output/dataframes/' + data_years[0] + '/album_age.csv',index_col=0).loc[:,'1':'200'])
df2 = get_album_age_df(pd.read_csv('output/dataframes/' + data_years[1] + '/album_age.csv',index_col=0).loc[:,'1':'200'])
df1.plot(ax=ax1, figsize=(12,4))
df2.plot(ax=ax1, figsize=(12,4))
ax1.legend(data_years)

ax2 = fig.add_subplot(122, title = 'Average Age Of Tracks', xlabel = 'Track rank', ylabel = 'Album Age (days)')
df3 = get_track_age_df(pd.read_csv('output/dataframes/' + data_years[0] + '/album_age.csv',index_col=0).loc[:,'1':'200'])
df4 = get_track_age_df(pd.read_csv('output/dataframes/' + data_years[1] + '/album_age.csv',index_col=0).loc[:,'1':'200'])
df3.plot(ax=ax2, figsize=(12,4))
df4.plot(ax=ax2, figsize=(12,4))
ax2.legend(data_years)

fig.savefig('output/figures/all/album_age.png')
