import pandas as pd
import matplotlib.pyplot as plt

def read_floats(filename):
    with open(filename) as f:
        return [float(x) for x in f]

def get_average_df(year):
    input_file = 'output/text/' + year + '/weekly_average_' + selected_param + '.txt'
    weekly_param_list = read_floats(input_file)
    
    list_of_weeks = ['week'] * 52
    for j in range(len(list_of_weeks)):
        list_of_weeks[j] += ' ' + str(j+1)
    
    df = pd.DataFrame()
    df['Weeks']  = list_of_weeks
    df[selected_param] = weekly_param_list
    return df

def group_weeks(df,param):
    df_grouped = pd.DataFrame(columns=[param])
    for i in range(0,52,4): #Groups 52 weeks into 13 groups of 4 weeks
        row = list(df.iloc[i:i+4].mean())
        df_grouped.loc[len(df_grouped)+1] = row
    return df_grouped

params_to_plot = ["duration_ms", "acousticness", "danceability", "energy", "instrumentalness", "liveness", "loudness", "speechiness", "valence", "tempo"]

for i in params_to_plot:
    selected_param = i
    
    df1 = group_weeks(get_average_df('2017'),selected_param)
    df2 = group_weeks(get_average_df('2018'),selected_param)
    
    ax = df1.plot(title=str('Weekly Average Of ' + selected_param), legend=True)
    plot = df2.plot(ax=ax)
    plot.set_xlabel("Group of 4 weeks")
    plt.legend(['2017','2018'])

    fig = plot.get_figure()
    fig.savefig('output/figures/all/weekly_average_' + selected_param + '.png')