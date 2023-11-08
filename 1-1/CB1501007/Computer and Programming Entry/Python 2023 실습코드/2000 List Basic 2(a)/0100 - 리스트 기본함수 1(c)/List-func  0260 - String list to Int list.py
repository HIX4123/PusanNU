#-------------------------------------------------------------------------------
# Purpose:     2020 컴퓨터및 프로그래밍 입문
# Author:      Cho
# Created:     2020-04-01
#-------------------------------------------------------------------------------

# initializing list
slist = ['1', '4', '3', '6', '7']
ilist=[]

# Printing original list
print ("Original list is : " + str(slist))

# for loop을 이용해서 출력하기
for i in range(0, len(slist)):
    ilist.append(0)
    ilist[i] = int(slist[i])

print("ilist= ", ilist, sum(ilist)  )

# List comprehension을 이용하는 방법
klist = [int(i) for i in slist]
print("klist= ", klist, sum(klist) )


# 함수형 언어의 기능인 map()을 이용하는 방법

mlist = list( map       (int,        slist))
#             map하라.  사용함수, 사용대상
print("mlist= ", mlist, sum(mlist) )

