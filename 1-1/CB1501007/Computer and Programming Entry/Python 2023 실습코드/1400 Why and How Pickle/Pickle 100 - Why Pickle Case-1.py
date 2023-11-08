# pickle.load(파일) 을 통해서 파일 내용을 읽어오려면,
# pickle.dump를 사용해서 데이터를 입력한 파일이어야한다.

import pickle
import string



with open('Someshop.txt',encoding='cp949') as f:
    shopname = f.read().splitlines()


print(f" 총 상가이름의 수 = {len(shopname)}")

Kshop=[]
myword = "우리"

count = 0
for w in shopname :
    if myword in w  :
        count += 1
        Kshop.append( w )
        print(f" {count:4}, {w}")


txtout = open('./data/Ourshop.txt', 'w',encoding='cp949')
for w in Kshop :
    print( w, file=txtout )

txtout.close()

outfile = open('./data/Ourshop.bin', 'wb')
pickle.dump( Kshop, outfile ) #python 내부에서 사용하는 형식 그대로 저장.
outfile.close( )











