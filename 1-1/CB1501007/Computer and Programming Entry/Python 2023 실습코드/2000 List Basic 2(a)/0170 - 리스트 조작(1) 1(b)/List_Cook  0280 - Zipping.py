#-------------------------------------------------------------------------------
# Purpose:     2020 컴퓨터및 프로그래밍 입문
# Author:      Cho
# Created:     2020-04-23
#-------------------------------------------------------------------------------


la = list("Computer")
lb = list("1234567890")
lc = list("부산갈매기만세")

# 자꾸..zipper.....

for (a,b,c) in zip(la,lb,lc) :
    w = (a,b,c)
    print(w)


dname=list("월화수목금토일")
ename="Mon Thu Wed Thu Fri Sat Sun".split()

pairs=[]
for Q in zip(dname,ename) :
    pairs.append(Q)


