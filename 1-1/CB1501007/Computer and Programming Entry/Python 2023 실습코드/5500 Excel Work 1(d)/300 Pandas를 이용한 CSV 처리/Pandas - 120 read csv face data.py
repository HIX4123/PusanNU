#-------------------------------------------------------------------------------
# Purpose:     2020 Prof. Zoh's Work
# Author:      Cho
# Created:     2020-06-29
#-------------------------------------------------------------------------------

# csv를 저장할 때는 반드시 unicode/utf-8로 저장해야 함.

import pandas as pd
landmarks = pd.read_csv('faces/face_landmarks.csv')

print( landmarks.loc[:,'image_name'] )

print(landmarks.loc[:,'image_name'].values)

print(landmarks.iloc[:,0].values)

