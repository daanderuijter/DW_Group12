import pandas as pd
import matplotlib.pyplot as plt

def read_floats(filename):
    with open(filename) as f:
        return [float(x) for x in f]

data_year = '2018'
params_to_plot = ["duration_ms", "acousticness", "danceability", "energy", "instrumentalness", "loudness", "speechiness", "valence", "tempo"] # Liveness is excluded here

fig, axes = plt.subplots(nrows=3, ncols=3)
plotcount = 0
for x_index in range(3):
    for y_index in range(3):
        selected_param = params_to_plot[plotcount]
        
        input_file = 'output/text/' + data_year + '/weekly_average_' + selected_param + '.txt'
        weekly_param_list = read_floats(input_file)

        list_of_weeks = ['week'] * 52
        for i in range(len(list_of_weeks)):
            list_of_weeks[i] += ' ' + str(i+1)
        
        df = pd.DataFrame()
        df['Weeks']  = list_of_weeks
        df[selected_param] = weekly_param_list
        
        df.plot(ax=axes[x_index,y_index], figsize=(30,18), title=str('Weekly Average Of ' + selected_param + ' In ' + data_year), legend=False)
        plotcount += 1

fig.savefig('output/figures/' + data_year + '/weekly_average_3_3.png')