
# 모기 유전자 서열(Genomic Sequence) 분석하기

import sys

f = open('mogi-dna-01.inp')
title = f.readline()
print("1. 염색체 이름 =", title[1:].rstrip())

pattern = input('Type DNA pattern : ')
print("2. 패턴 =", pattern)

line = ''               # 빈 문자열(변수만 생성), 문자열은 없는 null string
for inpstr in f:        # 각 줄별 문자열을 붙혀서 하나의 문자열로 만듬
    inpstr = inpstr.rstrip()
    line += inpstr

line = line.upper()     # 문자열을 모두 대문자로 바꿈.
print("3. 빈도수 =", line.count(pattern))

print("4. 위치")
prev = 0
howmany = line.count(pattern)
for k in range( howmany ):
    here = line.find( pattern, prev,-1)
    print(k,"번째 패턴의 위치", here)
    prev = here + 1     # 찾은 구역을 다음으로 넘긴다. 이전 검사구역을 증가시킴
                        # 이 방법은 중복을 허용해서 찾아주는 기능을 수행한다.


