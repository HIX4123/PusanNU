#-------------------------------------------------------------------------------
# Purpose:     2022 Zoh's Work     "過猶不及" 메롱..
# Author:      Cho
# Created:     2022-03-23
#-------------------------------------------------------------------------------

# 이미 "우리"가 상호명에 들어간 List를 바로
# 받아서 읽고 작업을 시작함.

import pickle

fin = open("./data/Ourshop.bin", "rb") # 2 mega

R = pickle.load(fin)
for w in R :
    if len(w) >= 12 :
        print(w)

print("=================")
for i,w in enumerate(R) :
    if '의원' in w  :
        print(f"{i:4}, {w}")


fin.close()