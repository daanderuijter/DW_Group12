'''
Loops through the dataframes containing the weekly averages for a given year and plots them individually
'''
import pandas as pd

data_year = '2018'
params_to_plot = ["duration_ms", "acousticness", "danceability", "energy", "instrumentalness", "liveness", "loudness", "speechiness", "valence", "tempo"]

for i in params_to_plot:
    
    selected_param = i
    df = pd.read_csv('output/dataframes/' + data_year + '/' + selected_param + '.csv', index_col=0)
    
    plot = df.plot(title=str('Weekly Average Of ' + selected_param + ' In ' + data_year), legend=False)
    plot.set_xlabel("Week")
    fig = plot.get_figure()
    fig.savefig('output/figures/' + data_year + '/weekly_average_' + selected_param + '.png')
