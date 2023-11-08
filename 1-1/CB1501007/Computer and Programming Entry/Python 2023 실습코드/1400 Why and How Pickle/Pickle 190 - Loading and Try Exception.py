#-------------------------------------------------------------------------------
# Purpose:     2020 컴퓨터및 프로그래밍 입문
# Author:      Cho
# Created:     2020-04-16
#-------------------------------------------------------------------------------

# pickle.load(파일) 을 통해서 파일 내용을 읽어오려면,
# pickle.dump를 사용해서 데이터를 입력한 파일이어야한다.

import pickle

with open('./data/Qic.bin', 'rb') as ifile :

    data_list = []
    while True:
        try:
          data = pickle.load(ifile)
        except EOFError:
            break

        data_list.append(data)

print( "Lading > Out", data_list )


ifile.close( )








