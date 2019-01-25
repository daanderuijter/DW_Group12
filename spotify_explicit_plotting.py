import matplotlib.pyplot as plt
import pandas as pd

data_year = '2017'
df = pd.read_csv('output/dataframes/' + data_year + '/explicit.csv',index_col=0)

df_grouped = pd.DataFrame(columns=list(df))
for i in range(0,52,4): #Groups 52 weeks into 13 groups of 4 weeks
    row = df.iloc[i:i+4].mean()
    df_grouped.loc[len(df_grouped)+1] = row

fig = plt.figure()

ax1 = fig.add_subplot(121)
ax1.set_title('Count Of Explicit Songs In ' + data_year)
ax1.set_xlabel('Group of 4 weeks')
ax1.set_ylabel('Count')
ax1.set_ylim(0,200)

ax2 = fig.add_subplot(122)
ax2.set_title('Mean Of Explicit Songs In ' + data_year)
ax2.set_xlabel('Group of 4 weeks')
ax2.set_ylabel('Mean')
ax2.set_ylim(0,200)

df_grouped['count_false'].plot(ax=ax1, figsize=(18,10), legend=True, label='False')
df_grouped['count_true'].plot(ax=ax1, figsize=(18,10),legend=True, label='True')

df_grouped['mean_false'].plot(ax=ax2, figsize=(18,10),legend=True, label='False')
df_grouped['mean_true'].plot(ax=ax2, figsize=(18,10),legend=True, label='True')

fig.savefig('output/figures/' + data_year + '/explicit.png')