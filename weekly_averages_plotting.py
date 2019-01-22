import pandas as pd

def read_floats(filename):
    with open(filename) as f:
        return [float(x) for x in f]

params_to_plot = ["duration_ms", "acousticness", "danceability", "energy", "instrumentalness", "liveness", "loudness", "speechiness", "valence", "tempo"]
selected_param = params_to_plot[0]  # 0-9

input_file = 'output/text/weekly_average_' + selected_param + '.txt'
weekly_param_list = read_floats(input_file)

print(weekly_param_list)
list_of_weeks = ['week'] * 52
for i in range(len(list_of_weeks)):
    list_of_weeks[i] += ' ' + str(i+1)

df = pd.DataFrame()
df['Weeks']  = list_of_weeks
df[selected_param] = weekly_param_list

plot = df.plot()
fig = plot.get_figure()
fig.savefig('output/figures/weekly_average_' + selected_param + '.png')