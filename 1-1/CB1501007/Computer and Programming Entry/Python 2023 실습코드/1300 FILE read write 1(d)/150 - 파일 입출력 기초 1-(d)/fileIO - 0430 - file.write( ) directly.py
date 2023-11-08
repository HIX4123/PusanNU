#-------------------------------------------------------------------------------
# Purpose:     2019 Power Python
# Author:      Cho
#-------------------------------------------------------------------------------


# writedata.py
myf = open("./data/kukeul.txt", 'w')

for i in range(1, 11):
    data = "%d번째 줄입니다.\n" % i
    myf.write(data)  # print(data, file= myf) 과 동일

myf.close()