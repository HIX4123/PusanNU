#-------------------------------------------------------------------------------
# Purpose:     2020 컴퓨터및 프로그래밍 입문
# Author:      Cho
# Created:     2020-04-16
#-------------------------------------------------------------------------------
# https://wayhome25.github.io/cs/2017/04/04/cs-04/

import pickle

f = open('./data/goodbeer.txt', 'wb')
pickle.dump('hello world', f)   #string 덤프
pickle.dump(12345, f)           #int 덤프
pickle.dump(3.14, f)            #float 덤프
pickle.dump(['one', 'two', 'three', 'four'], f) #list 덤프
pickle.dump({1:'first', 2:'second'}, f) #dict 덤프
f.close()

f = open('./data/goodbeer.txt', 'rb')
d = pickle.load(f) #string 로드
print(type(d))
print(d)
d = pickle.load(f) #int 로드
print(type(d))
print(d)
d = pickle.load(f) #float 로드
print(type(d))
print(d)
d = pickle.load(f) #list 로드
print(type(d))
print(d)
d = pickle.load(f) #dict 로드
print(type(d))
print(d)
f.close()