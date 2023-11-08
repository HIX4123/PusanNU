# 어떤 집합에서 원소의 존재여부를 확인할 때
# 두가지 방법. 리스트와 집합

# 두 방법의 결과는 같으나 hashing이 가능한 집합(Set)이 더 빠르다.
# 더 빠르다고

import time
import random
import array as arr
N= 20000

mylist  =[]  # 정렬이 안된 리스트
sortlist=[]  # 원소를 오름차순으로 정렬
mydict  ={}  # 사전
myset   = set()
myarray = arr.array('d', [])
qlist   =[]  # Query data 찾아보기에 사용할 데이터를 저장한 리시트

for w in range(N): # 각 데이터별 준비
    rval = random.randint(0,2*N) # 무작위값 10N이면 set이 더 빠름
    mylist.append(rval)
    myset.add(rval)
    if rval in mydict.keys():
        mydict[rval]+= 1
    else :
        mydict[rval]= 1
    myarray.append(rval)

    qval = random.randint(0,2*N) # 새로운 무작위 값
    qlist.append(qval)

print(f" Step1. 모든 {N}개의 데이터가  준비되었음")


sortlist=sorted( mylist)

def lookup_array(x):
    return x in myarray

def lookup_set(x):
    return x in myset

def lookup_sort(x):
    return x in sortlist

def lookup_list(x):
    return x in mylist

def lookup_dict(x):
    return x in mydict

tbegin= time.process_time()
for w in  qlist :
    lookup_list(w)
tend = time.process_time()
print( f'N={ N:7} 정렬이 안된 List에서 검사= {tend-tbegin:10.7f} sec.')

tbegin= time.process_time()
for w in  qlist :
    lookup_sort(w)
tend = time.process_time()
print( f'N={ N:7} 정렬된 List에서 검사= {tend-tbegin:10.7f} sec.')

tbegin= time.process_time()
for w in  qlist :
    lookup_dict(w)
tend = time.process_time()
print( f'N={ N:7} dict에서 검사= {tend-tbegin:10.7f} sec.')


tbegin= time.process_time()
for w in  qlist :
    lookup_set(w)
tend = time.process_time()
print( f'N={ N:7}  set에서 검사= {tend-tbegin:10.7f} sec.')


tbegin= time.process_time()
for w in  qlist :
    lookup_array(w)
tend = time.process_time()
print( f'N={ N:7} array에서 검사= {tend-tbegin:10.7f} sec.')
