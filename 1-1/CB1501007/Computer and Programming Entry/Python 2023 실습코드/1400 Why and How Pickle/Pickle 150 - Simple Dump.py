#-------------------------------------------------------------------------------
# Purpose:     2020 컴퓨터및 프로그래밍 입문
# Author:      Cho
# Created:     2020-04-16
#-------------------------------------------------------------------------------

# pickle.load(파일) 을 통해서 파일 내용을 읽어오려면,
# pickle.dump를 사용해서 데이터를 입력한 파일이어야한다.

import pickle

mydic = [ 45<78 , {'john': 25, "메롱":78}, list("갈매기"), {'yang': 50} ]


ofile = open('./data/Qic.bin', 'wb')

for data in mydic :  #넣을 때에는 한 원소씩 넣을 수 있다.
    pickle.dump(data, ofile)


ofile.close( )








