#-------------------------------------------------------------------------------
# Purpose:     2020 컴퓨터및 프로그래밍 입문
# Author:      Cho
# Created:     2020-04-16
#-------------------------------------------------------------------------------



import pickle

file = open('./data/List_dump.bin', 'rb')
data = pickle.load(file)
file.close() # close the file

print('Showing the pickled data:')

cnt = 0
for item in data:
    print('The data ', cnt, ' is : ', item, "type=", type(item))
    cnt += 1

