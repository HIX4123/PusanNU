#-------------------------------------------------------------------------------
# Purpose:     2020 컴퓨터및 프로그래밍 입문
# Author:      Cho
# Created:     2020-05-25
#-------------------------------------------------------------------------------


import os
from pathlib import Path

path = '.' # 현재 이 py code가 있는 위치
obj = os.scandir()

print( f' 화일과 폴더 in {path}')

for entry in obj :
    if entry.is_file():
            print( f'name= { entry.name }', end=" ")
            print( ", EXT=", Path( entry.name ).suffix )
            # print( "==>", Path( entry.name ).suffixes ) #a.zip.tar





obj.close()


