import matplotlib.pyplot as plt
import pandas as pd

def get_explicit_df(year):
    df = pd.read_csv('output/dataframes/' + year + '/explicit.csv',index_col=0)
    return df

def group_weeks(df):
    df_grouped = pd.DataFrame(columns=list(df))
    for i in range(0,52,4): #Groups 52 weeks into 13 groups of 4 weeks
        row = df.iloc[i:i+4].mean()
        df_grouped.loc[len(df_grouped)+1] = row
    return df_grouped

df1 = group_weeks(get_explicit_df('2017'))
df2 = group_weeks(get_explicit_df('2018'))

fig = plt.figure()

ax1 = fig.add_subplot(121)
ax1.set_title('Count Of Explicit Songs')
ax1.set_xlabel('Group of 4 weeks')
ax1.set_ylabel('Count')
ax1.set_ylim(0,200)

ax2 = fig.add_subplot(122)
ax2.set_title('Mean Of Explicit Songs')
ax2.set_xlabel('Group of 4 weeks')
ax2.set_ylabel('Mean')
ax2.set_ylim(0,200)

df1['count_true'].plot(ax=ax1, figsize=(18,10),legend=True, label='2017')
df2['count_true'].plot(ax=ax1, figsize=(18,10),legend=True, label='2018')

df1['mean_true'].plot(ax=ax2, figsize=(18,10),legend=True, label='2017')
df2['mean_true'].plot(ax=ax2, figsize=(18,10),legend=True, label='2018')

fig.savefig('output/figures/all/explicit.png')