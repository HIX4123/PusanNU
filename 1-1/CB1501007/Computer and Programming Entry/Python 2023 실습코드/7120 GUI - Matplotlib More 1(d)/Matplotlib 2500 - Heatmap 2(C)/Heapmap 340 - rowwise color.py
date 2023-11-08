#-------------------------------------------------------------------------------
# Name:        module1
# Author:      algor
#-------------------------------------------------------------------------------

import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

d = {'jan': [44,  2,  3,  4],
     'feb': [33,  4,  6,  8],
     'mar': [50, 10, 15, 20],
     'abr': [11, 12, 13, 14],
     'mai': [ 3, 40,  6, 60],
     'jun': [40,  8, 12, 16]}

idx = ['A', 'B', 'C', 'D']

df = pd.DataFrame(d, index = idx)
cm = ['Blues', 'Reds', 'Greens', 'Purples']
f, axs = plt.subplots(4, 1, gridspec_kw={'hspace': 0})

counter = 0
for index, row in df.iterrows():
    sns.heatmap(np.array([row.values]), yticklabels=[idx[counter]], xticklabels=df.columns, annot=True, fmt='.2f', ax=axs[counter], cmap=cm[counter], cbar=False)
    counter += 1

plt.show()