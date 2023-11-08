#-------------------------------------------------------------------------------
# Name:        module1
# Author:      algor
#-------------------------------------------------------------------------------

import matplotlib.pyplot as plt
import matplotlib.colors as mcl
import seaborn as sns

import numpy as np
import pandas as pd

from matplotlib.colors import LinearSegmentedColormap

## 데이터 생성데이터 생성
np.random.seed(5)
columns = ['X' + str(x).zfill(2) for x in range(10)]

data = {}
for k in columns:
    data[k] = [0]*20

map_df = pd.DataFrame(data)
map_df.index = ['Y' + str(x).zfill(2) for x in range(20)]

for i in range(map_df.shape[0]):
    for j in range(map_df.shape[1]):
        map_df.iloc[i,j] = np.random.randn(1)



fig = plt.figure(figsize=(6,6)) # 6인치 by 6 인치
fig.set_facecolor('white')

h = 24
s = 0.99
v = 1

colors = [
    mcl.hsv_to_rgb((h/360,0,v)),
    mcl.hsv_to_rgb((h/360,0.5,v)),
    mcl.hsv_to_rgb((h/360,1,v))
]
cmap = LinearSegmentedColormap.from_list('my_cmap',colors,gamma=3)


#sns.heatmap(round_func(map_df.values),cmap=cmap,annot=True)
sns.heatmap( np.round(map_df.values,1) ,cmap=cmap, annot=True)
#                      1자리 반올림


plt.xticks( range(len(map_df.columns)),map_df.columns) ## x축 눈금 생성
plt.yticks( range(len(map_df.index)), map_df.index) ## y축 눈금 생성

plt.show()