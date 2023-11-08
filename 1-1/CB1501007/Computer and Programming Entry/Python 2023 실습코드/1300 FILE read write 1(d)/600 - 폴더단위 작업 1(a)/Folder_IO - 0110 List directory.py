

import os
import glob


print("모든 python 화일들")
myfiles =  glob.glob('*.py')
for w in myfiles :
    print(w)

print("\n\n 화일이름에 sys를 포함한 모든 화일들")
myfiles =  glob.glob('*sys*.py')
for w in myfiles :
    print(w)

os.chdir('data')
print("\n\n 모든 ./data/ 아래에 있는 모든 *.txt 화일들")
myfiles =  glob.glob('*.txt')
for w in myfiles :
    print(w)

print("\n\n 현재 이 프로그램이 수행되는 directory에 있는 모든 화일들")
allfiles = os.listdir('.')
for w in allfiles :
    print(w)