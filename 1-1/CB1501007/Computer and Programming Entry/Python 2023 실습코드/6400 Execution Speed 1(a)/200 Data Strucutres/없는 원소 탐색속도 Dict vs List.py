
# 카라마조프가의 형제들 소설 일부를 읽어서 탐색 속도를
# 리스트와 dict 기준으로 비교함.
import time
import random

def lookup_list(x, L ):
    return x in L

def lookup_dict(x, D):
    return x in D

def List_to_Dict( L) :
    D={}
    for w in L :
        if w in D.keys() :
            D[w] += 1
        else : # 없는 경우
            D[w] = 1
    return( D )



f = open("Karamazov.txt", 'r',encoding='cp949')


mydata = f.read( )
f.close()

print("> Karamazov.txt의 길이 = ",  len(mydata))
print("> Karamazov.txt Enter  수= ",  mydata.count("\n") )


single = mydata.replace("\n"," ")
print("> 한 줄로 만든 Karamazov의 길이 = ", len( single ))

KaraList = single.split( )
print("> Karamazov에 존재하는 단어의 갯수= ", len(KaraList))

KaraDict = List_to_Dict( KaraList )

N=10000
tbegin= time.process_time()
for w in  range(N):
    lookup_dict("NoNo", KaraDict )
tend = time.process_time()
print( f'N={ N:7} dict에서 없는 원소 검사= {tend-tbegin:10.7f} sec.')

tbegin= time.process_time()
for w in  range(N):
    lookup_list("NoNo" , KaraList)
tend = time.process_time()
print( f'N={ N:7} list에서 없는 원소 검사= {tend-tbegin:10.7f} sec.')

