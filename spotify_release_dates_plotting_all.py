import matplotlib.pyplot as plt
import pandas as pd

def get_release_date_df(year):
    df = pd.read_csv('output/dataframes/' + year + '/release_date.csv',index_col=0).loc[:,'1':'200']
    return df

def get_album_age_df(df):
    album_df = pd.DataFrame(columns=list(range(1,201)))
    
    for i in range(0,52,4): #Groups 52 weeks into 13 groups of 4 weeks
        row = list(df.iloc[i:i+4].mean())
        album_df.loc[len(album_df)+1] = row
    return album_df

def get_track_age_df(df):
    track_df = pd.DataFrame(columns=['mean age'])

    for i in range(1,200,10): #Groups Top 200 into 20 groups of 10 tracks
        row = df.loc[:,str(i):str(i+9)].mean().mean()
        track_df.loc[i] = row
    return track_df

fig = plt.figure()
ax1 = fig.add_subplot(121)
ax1.set_title('Average Age Of Albums')
ax1.set_xlabel('Group of 4 weeks')
ax1.set_ylabel('Album Age (days)')

df1 = get_album_age_df(get_release_date_df('2017'))
df2 = get_album_age_df(get_release_date_df('2018'))
df1.transpose().mean().plot(ax=ax1, figsize=(12,4))
df2.transpose().mean().plot(ax=ax1, figsize=(12,4))
ax1.legend(['2017','2018'])

ax2 = fig.add_subplot(122)
ax2.set_title('Average Age Of Tracks')
ax2.set_xlabel('Track rank')
ax2.set_ylabel('Album Age (days)')

df3 = get_track_age_df(get_release_date_df('2017'))
df4 = get_track_age_df(get_release_date_df('2018'))
df3.plot(ax=ax2, figsize=(12,4))
df4.plot(ax=ax2, figsize=(12,4))
ax2.legend(['2017','2018'])

fig.savefig('output/figures/all/track_age.png')