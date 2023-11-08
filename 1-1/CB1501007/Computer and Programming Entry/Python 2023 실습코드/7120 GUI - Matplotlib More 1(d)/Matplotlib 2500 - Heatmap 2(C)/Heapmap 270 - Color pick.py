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

h = 24   #HSV color space
s = 0.99
v = 1

# https://imagecolorpicker.com/ 에서 색깔을 찍어서 성분을 확인한다.
# 구글에서 color picker를 찾아서 색상을 확인한다.

colors = [
    mcl.hsv_to_rgb((h/360,  0,v)),
    mcl.hsv_to_rgb((h/360,0.5,v)),
    mcl.hsv_to_rgb((h/360,  1,v))
]

colors = [ '#FA0AE3', '#3425F0']
# RGB로 설정할 수 있다.
cmap = LinearSegmentedColormap.from_list('my_cmap',colors, gamma=3)

fig = plt.figure(figsize=(6,6))
fig.set_facecolor('white')


plt.xticks(range(len(map_df.columns)),map_df.columns) ## x축 눈금 생성
plt.yticks(range(len(map_df.index)), map_df.index) ## y축 눈금 생성


plt.pcolor( map_df.values, cmap=cmap)
plt.xticks( range(len(map_df.columns)),map_df.columns) ## x축 눈금 생성
plt.yticks( range(len(map_df.index)), map_df.index) ## y축 눈금 생성

plt.colorbar()  # 이것이 핵심, seaborn을 사용하지 않는 경우
plt.show()