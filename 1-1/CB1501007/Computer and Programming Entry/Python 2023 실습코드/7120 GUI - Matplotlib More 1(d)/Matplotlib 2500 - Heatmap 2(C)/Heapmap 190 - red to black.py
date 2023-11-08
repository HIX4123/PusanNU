#-------------------------------------------------------------------------------
# Name:        module1
# Author:      algor
#-------------------------------------------------------------------------------
# https://www.python-graph-gallery.com/heatmap/
# 3월 24일 금요일 오전

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

from  matplotlib.colors import LinearSegmentedColormap
mymap=LinearSegmentedColormap.from_list('kr',["k", "w", "r"], N=256)

# Create a dataset
df = pd.DataFrame(np.random.random((10,10)), columns=["a","b","c","d","e","f","g","h","i","j"])

# plot using a color palette
sns.heatmap(df, cmap=mymap)
plt.show()

##sns.heatmap(df, cmap="Blues")
##plt.show()
##
##sns.heatmap(df, cmap="BuPu")
##plt.show()
##
##sns.heatmap(df, cmap="Greens")
##plt.show()