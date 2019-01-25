import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('output/dataframes/release_date.csv',index_col=0).loc[:,'1':'200']

mycolumns1 = list(range(1,201))
df2 = pd.DataFrame(columns=mycolumns1)
mycolumns2 = ['mean age']
df3 = pd.DataFrame(columns=mycolumns2)

for i in range(0,52,4): #Groups 52 weeks into 13 groups of 4 weeks
    row = list(df.iloc[i:i+4].mean())
    df2.loc[len(df2)+1] = row
    
for i in range(1,200,10): #Groups Top 200 into 20 groups of 10 tracks
    row = df.loc[:,str(i):str(i+9)].mean().mean()
    df3.loc[i] = row
    
fig = plt.figure()
ax1 = fig.add_subplot(121)
ax1.set_title('Average Age Of Albums By Month')
ax1.set_xlabel('Group of 4 weeks')
ax1.set_ylabel('Album Age (days)')
df2.transpose().mean().plot(ax=ax1, figsize=(12,4))

ax2 = fig.add_subplot(122)
ax2.set_title('Average Age Of Tracks By Rank')
ax2.set_xlabel('Track rank')
ax2.set_ylabel('Album Age (days)')
df3.plot(ax=ax2, figsize=(12,4))

fig.savefig('output/figures/track_age.png')