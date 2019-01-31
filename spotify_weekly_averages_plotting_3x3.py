'''
Loops through the dataframes containing the weekly averages for a given year and plots them in a single 3x3 plot
'''
import pandas as pd
import matplotlib.pyplot as plt

params_to_plot = ["duration_ms", "acousticness", "danceability", "energy", "instrumentalness", "loudness", "speechiness", "valence", "tempo"] # Liveness is excluded here

data_years = ['2017','2018']
for year in data_years:

    fig, axes = plt.subplots(nrows=3, ncols=3)
    plotcount = 0
    
    for x_index in range(3):
        for y_index in range(3):
            
            selected_param = params_to_plot[plotcount]
            df = pd.read_csv('output/dataframes/' + year + '/' + selected_param + '.csv', index_col=0)
            
            df.plot(ax=axes[x_index,y_index], figsize=(30,18), title=str('Weekly Average Of ' + selected_param + ' In ' + year), legend=False)
            plotcount += 1
    
    fig.savefig('output/figures/' + year + '/weekly_average_3_3.png')
