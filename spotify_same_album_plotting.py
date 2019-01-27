import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('output/dataframes/all/albums.csv',index_col=0)

fig = plt.figure()
plt.hist(df['unique_albums'],40)
plt.title('Histogram Of Number Of Unique Albums In US Top 200')
plt.xlabel('Unique albums')
plt.ylabel('N')

fig.savefig('output/figures/all/albums.png')