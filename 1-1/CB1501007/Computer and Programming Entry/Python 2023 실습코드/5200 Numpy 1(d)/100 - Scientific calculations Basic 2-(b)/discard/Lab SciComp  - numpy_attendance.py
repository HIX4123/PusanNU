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
print("�⼮��")
print(attendance_book)

print()
print("�л��� �⼮ ��Ȳ")

i=1
for row in attendance_book :
    print(i,"���л� �⼮�ϼ� :", np.sum(row),"/ 30")
    i +=1

print()
print("�Ϻ� �⼮ ��Ȳ")
for i in range(date) :
    print(i+1, "�� �⼮�ο� :",np.sum(attendance_book[:,i]))










