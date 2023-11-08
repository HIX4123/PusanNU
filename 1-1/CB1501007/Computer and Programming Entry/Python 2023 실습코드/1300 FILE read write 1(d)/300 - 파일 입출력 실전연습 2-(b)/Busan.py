# Problem Solving Class A
# 파일에 한 줄에 여러 개의 자료(token)이 있을 때
# 하나씩 token type으로 읽는 연습을 합니다.

import random

myfile  = open("Busan.txt" ,"r" , encoding='cp949')  # 읽을 파일을 준비 함
outfile = open("Busan_Out.txt" ,"w" , encoding='cp949')  # 읽을 파일을 준비 함

randaddr=[]
for oneline in myfile  :     # 한 라인씩 읽음
    addrs = oneline.split('|')
    astring =addrs[3]+addrs[4]+addrs[5]+addrs[7]+addrs[15]
    randaddr.append( astring )


i = 1
random.shuffle( randaddr )
for w in randaddr :
    print (f"{i:6} {w}", file=outfile)
    i += 1

myfile.close()  # 한번  연 화일은 반드시 닫아야만 됩니다.
outfile.close()
print("It is over.")