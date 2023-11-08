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

sns.heatmap(map_df,cmap='Reds')
#plt.pcolor( map_df.values, cmap='Reds')
plt.xticks( range(len(map_df.columns)),map_df.columns) ## x축 눈금 생성
plt.yticks( range(len(map_df.index)), map_df.index) ## y축 눈금 생성

#plt.colorbar()  # 이것이 핵심, seaborn을 사용하지 않는 경우
plt.show()