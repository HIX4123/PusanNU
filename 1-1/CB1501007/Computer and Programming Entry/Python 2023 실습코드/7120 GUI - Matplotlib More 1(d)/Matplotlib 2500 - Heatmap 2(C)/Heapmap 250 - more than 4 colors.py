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

# 중간 색상과 그 경계 값을 미세조정 가능함. 이게 제일 좋아보이는데

from  matplotlib.colors import LinearSegmentedColormap
c = ["darkred","red","lightcoral","white", "palegreen","green","darkgreen"]
v = [   0.0   ,.15,   .4,          .5,      0.6,        .9,     1.]
cl = list(zip(v,c))

mymap = LinearSegmentedColormap.from_list('More', cl, N=256)

# Create a dataset
df = pd.DataFrame(np.random.random((10,10)), columns=["a","b","c","d","e","f","g","h","i","j"])

# plot using a color palette
sns.heatmap(df, cmap=mymap)
plt.show()

