# 가게이름에서 특수문자를 걸러냄

import re
import pickle

ftxt =  open("small.txt", "r",encoding='cp949')


i=0
for line in ftxt:  #파일을 끝까지 읽고 자동적으로 마
    i += 1
    cline=line.strip()
    print( f'i={i:3},  {cline}')

ftxt.close()
