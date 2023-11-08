# FILE : mymoda.py
import importlib


import mymoda  # x.pyc가 있으면 이것을 가지고 옴. 없으면 x.py를 가지고 옴.
import mymodb
import mysymbol

importlib.reload(mymoda)  #이것을 끄고 한번 수행해 봅시다.
importlib.reload(mymodb)

#print area(10)  #누구의 함수일까요 ? 이 프로그램의 공간과 일치
print(mymoda.area(10))  # moda의 공간 , 결과는 같지만
print(mymodb.area(10))
#print goodpi,
print(mymodb.goodpi)
print("mymoda= ", mymoda.mystring)
print("mymodb= ", mymodb.mystring)
