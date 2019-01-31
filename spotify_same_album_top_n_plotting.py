'''
Loads the dataframes containing the weekly unique album values for every Top n<50 and plots them
'''
import matplotlib.pyplot as plt
import pandas as pd

n = 50
df = pd.read_csv('output/dataframes/all/albums_top_' + str(n) + '.csv',index_col=0)

fig = plt.figure()

plt.hist(df['unique_albums'],int(n/4))
plt.title('Histogram Of Number Of Unique Albums In US Top ' + str(n))
plt.xlabel('Unique albums')
plt.ylabel('N')

fig.savefig('output/figures/all/albums_top_' + str(n) + '.png')
