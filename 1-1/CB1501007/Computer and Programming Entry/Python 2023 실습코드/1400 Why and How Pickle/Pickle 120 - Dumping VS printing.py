#-------------------------------------------------------------------------------
# Purpose:     2020 컴퓨터및 프로그래밍 입문
# Author:      Cho
# Created:     2020-04-16
#-------------------------------------------------------------------------------

# pickle.load(파일) 을 통해서 파일 내용을 읽어오려면,
# pickle.dump를 사용해서 데이터를 입력한 파일이어야한다.

import pickle


my = [ 23, 45, 67, 89, 100 ]


outfile = open('./my.bin', 'wb')  # b는 binary를 의미
rawfile = open('./my.txt', 'w')

pickle.dump( my, outfile)
print( my, file=rawfile )


outfile.close( )
rawfile.close( )


mybin = open('./my.bin', 'rb')
Tmy = pickle.load( mybin )
for w in Tmy:
    print(w)
print(Tmy)

mytxt = open('my.txt', 'r', encoding='cp949' )
Tline = mytxt.readline()
print(Tline)
for w in Tline :
    print(w)










