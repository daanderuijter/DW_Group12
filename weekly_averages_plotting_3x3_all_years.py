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

params_to_plot = ["duration_ms", "acousticness", "danceability", "energy", "instrumentalness", "loudness", "speechiness", "valence", "tempo"] # Liveness is excluded here

fig, axes = plt.subplots(nrows=3, ncols=3)
plotcount = 0
for x_index in range(3):
    for y_index in range(3):
        selected_param = params_to_plot[plotcount]
        
        df1 = group_weeks(get_average_df('2017'),selected_param)
        df2 = group_weeks(get_average_df('2018'),selected_param)
        
        df1.plot(ax=axes[x_index,y_index], figsize=(30,18), title=str('Weekly Average Of ' + selected_param), legend=True)
        plot = df2.plot(ax=axes[x_index,y_index], figsize=(30,18), title=str('Weekly Average Of ' + selected_param))
        
        plot.set_xlabel("Group of 4 weeks")
        axes[x_index,y_index].legend(['2017','2018'])
        plotcount += 1

fig.savefig('output/figures/all/weekly_average_3_3.png')