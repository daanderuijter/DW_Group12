'''
Loops through the dataframes containing the weekly averages for a given list of years, groups the weeks and plots them in a single 3x3 plot
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
params_to_plot = ["duration_ms", "acousticness", "danceability", "energy", "instrumentalness", "loudness", "speechiness", "valence", "tempo"] # Liveness is excluded here

fig, axes = plt.subplots(nrows=3, ncols=3)
plotcount = 0
for x_index in range(3):
    for y_index in range(3):
        selected_param = params_to_plot[plotcount]
        
        df1 = group_weeks(df = pd.read_csv('output/dataframes/' + data_years[0] + '/' + selected_param + '.csv', index_col=0))
        df2 = group_weeks(df = pd.read_csv('output/dataframes/' + data_years[1] + '/' + selected_param + '.csv', index_col=0))
        
        df1.plot(ax=axes[x_index,y_index], figsize=(30,18), title=str('Weekly Average Of ' + selected_param), legend=True)
        plot = df2.plot(ax=axes[x_index,y_index], figsize=(30,18), title=str('Weekly Average Of ' + selected_param))
        
        plot.set_xlabel("Group of 4 weeks")
        axes[x_index,y_index].legend(data_years)
        plotcount += 1

fig.savefig('output/figures/all/weekly_average_3_3.png')
