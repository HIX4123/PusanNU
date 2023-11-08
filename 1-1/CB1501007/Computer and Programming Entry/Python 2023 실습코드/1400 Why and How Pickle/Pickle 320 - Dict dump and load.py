#-------------------------------------------------------------------------------
# Purpose:     2020 컴퓨터및 프로그래밍 입문
# Author:      Cho
# Created:     2020-04-16
#-------------------------------------------------------------------------------
"""
•일반 텍스트를 파일로 저장할 때는 파일 입출력을 이용한다.
•하지만 리스트나 클래스같은 텍스트가 아닌 자료형은 일반적인
 파일 입출력 방법으로는 데이터를 저장하거나 불러올 수 없다.
•파이썬에서는 이와 같은 텍스트 이외의 자료형을 파일로 저장하기 위하여
 pickle이라는 모듈을 제공한다.
"""

import pickle

D={}
D[1]="하나요"
D[2]="둘이요"
D[3]="세개요"
mlist = list("무궁화 꽃이 피었습니다.")



with open('./data/mydic.bin', 'wb') as outf:
    pickle.dump( D , outf )
    pickle.dump( mlist , outf )


with open('./data/mydic.bin', 'rb') as inf:
    data1 = pickle.load(inf) # 단 한줄씩 읽어옴
    data2 = pickle.load(inf) # 단 한줄씩 읽어옴

print("data= ", data1, data2  )

