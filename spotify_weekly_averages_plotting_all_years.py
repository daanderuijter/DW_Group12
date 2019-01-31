'''
Loops through the dataframes containing the weekly averages for a given list of years, groups the weeks and plots them individually
'''
import pandas as pd
import matplotlib.pyplot as plt

def group_weeks(df):
    df_grouped = pd.DataFrame(columns=[df.columns[1]])
    for i in range(0,52,4): #Groups 52 weeks into 13 groups of 4 weeks
        row = list(df.iloc[i:i+4].mean())
        df_grouped.loc[len(df_grouped)+1] = row
    return df_grouped

data_years = ['2017','2018']
params_to_plot = ["duration_ms", "acousticness", "danceability", "energy", "instrumentalness", "liveness", "loudness", "speechiness", "valence", "tempo"]

for i in params_to_plot:
    selected_param = i
    
    df1 = group_weeks(df = pd.read_csv('output/dataframes/' + data_years[0] + '/' + selected_param + '.csv', index_col=0))
    df2 = group_weeks(df = pd.read_csv('output/dataframes/' + data_years[1] + '/' + selected_param + '.csv', index_col=0))
    
    ax = df1.plot(title=str('Weekly Average Of ' + selected_param), legend=True)
    plot = df2.plot(ax=ax)
    
    plot.set_xlabel("Group of 4 weeks")
    plt.legend(data_years)

    fig = plot.get_figure()
    fig.savefig('output/figures/all/weekly_average_' + selected_param + '.png')
