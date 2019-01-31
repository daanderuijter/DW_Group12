'''
Loads the dataframes containing the weekly explicit song values for a given year and individually plots the count and mean rank
'''
import matplotlib.pyplot as plt
import pandas as pd

def group_weeks(df):
    df_grouped = pd.DataFrame(columns=list(df))
    for i in range(0,52,4): #Groups 52 weeks into 13 groups of 4 weeks
        row = df.iloc[i:i+4].mean()
        df_grouped.loc[len(df_grouped)+1] = row
    return df_grouped

data_years = ['2017','2018']
for year in data_years:
    df = group_weeks(pd.read_csv('output/dataframes/' + year + '/explicit.csv',index_col=0))
    
    fig = plt.figure()
    
    ax1 = fig.add_subplot(121, title = 'Count Of Explicit Songs In ' + year, xlabel = 'Group of 4 weeks', ylabel = 'Count')
    df['count'].plot(ax=ax1, figsize=(18,10))
    ax1.set_ylim(0,200)
    
    ax2 = fig.add_subplot(122, title = 'Mean Rank Of Explicit Songs In ' + year, xlabel = 'Group of 4 weeks', ylabel = 'Mean Rank')
    df['mean_rank'].plot(ax=ax2, figsize=(18,10))
    ax2.set_ylim(0,200)
    
    fig.savefig('output/figures/' + year + '/explicit.png')
