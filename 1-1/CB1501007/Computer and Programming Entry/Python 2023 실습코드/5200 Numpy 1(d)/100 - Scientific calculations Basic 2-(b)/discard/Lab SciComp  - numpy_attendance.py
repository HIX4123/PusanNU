#-*- coding:cp949 -*-

import numpy as np

fin = open('attendance.inp', 'r')

temp = fin.readline()
tlist = temp.split()

student = int(tlist[1])
date = int(tlist[0])


attendance_book = np.zeros((student,date),int)

while(temp!="") :
    temp = fin.readline()
    tlist = temp.split()
    i = 1;
    try :
        while(int(tlist[i])!=0) :
            attendance_book[int(tlist[i])-1][int(tlist[0])-1] = 1
            i +=1
    except IndexError :
        print("", end=' ')
print("출석부")
print(attendance_book)

print()
print("학생별 출석 현황")

i=1
for row in attendance_book :
    print(i,"번학생 출석일수 :", np.sum(row),"/ 30")
    i +=1

print()
print("일별 출석 현황")
for i in range(date) :
    print(i+1, "일 출석인원 :",np.sum(attendance_book[:,i]))










