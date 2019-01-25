import pandas as pd

def read_floats(filename):
    with open(filename) as f:
        return [float(x) for x in f]

data_year = '2018'
params_to_plot = ["duration_ms", "acousticness", "danceability", "energy", "instrumentalness", "liveness", "loudness", "speechiness", "valence", "tempo"]

for i in params_to_plot:
    selected_param = i

    input_file = 'output/text/' + data_year + '/weekly_average_' + selected_param + '.txt'
    weekly_param_list = read_floats(input_file)
    
    list_of_weeks = ['week'] * 52
    for j in range(len(list_of_weeks)):
        list_of_weeks[j] += ' ' + str(j+1)
    
    df = pd.DataFrame()
    df['Weeks']  = list_of_weeks
    df[selected_param] = weekly_param_list
    
    plot = df.plot(title=str('Weekly Average Of ' + selected_param + ' In ' + data_year), legend=False)
    plot.set_xlabel("Week")
    fig = plot.get_figure()
    fig.savefig('output/figures/' + data_year + '/weekly_average_' + selected_param + '.png')