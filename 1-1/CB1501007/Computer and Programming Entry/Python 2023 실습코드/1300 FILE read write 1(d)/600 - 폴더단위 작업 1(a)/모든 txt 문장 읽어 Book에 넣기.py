#-------------------------------------------------------------------------------
# Purpose:     2020 컴퓨터및 프로그래밍 입문
# Author:      Cho
# Created:     2020-05-25
#-------------------------------------------------------------------------------


import os

mypath = "./data"
os.chdir( mypath )
obj = os.scandir( )  # 아래 folder로 간다.

Book=[]

print( f' 탐색하는 폴더 : { mypath}')

count= 0
Lines = 0
for entry in obj :
    count += 1
    if entry.is_file():
        if entry.name[-4:]== r'.txt' :  # *.txt만 선택한다.
            print( f" {count}. file= {entry.name}")
            fin = open( entry.name, "r",  encoding='utf-8' )# 이걸 조심. 파일형식
            fsize = os.path.getsize( entry.name )
            print(f" fsize = {fsize}" )
            while True:  # 계속 작업을 수행한다.
                line = fin.readline()
                #print(f"line= {line}")
                Book.append( line )
                Lines += 1
                if( line == '') :       # 마지막 줄 검사. 반드시 뒷줄에 빈 return문자
                    print( f" 입력 파일 다 읽음: 쌓인 라인수= { Lines }")
                    break   #While Loop을 빠져 나간다. break the while Loop
            fin.close()


obj.close()


