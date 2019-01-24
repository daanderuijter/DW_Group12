import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('output/dataframes/explicit.csv',index_col=0)

fig = plt.figure()

ax1 = fig.add_subplot(121)
ax1.set_title('Count Of Explicit Songs')
ax1.set_xlabel('week')
ax1.set_ylabel('count')

ax2 = fig.add_subplot(122)
ax2.set_title('Mean Of Explicit Songs')
ax2.set_xlabel('week')
ax2.set_ylabel('mean')

df['count_false'].plot(ax=ax1, figsize=(18,10), legend=True, label='False')
df['count_true'].plot(ax=ax1, figsize=(18,10),legend=True, label='True')

df['mean_false'].plot(ax=ax2, figsize=(18,10),legend=True, label='False')
df['mean_true'].plot(ax=ax2, figsize=(18,10),legend=True, label='True')

fig.savefig('output/figures/explicit.png')