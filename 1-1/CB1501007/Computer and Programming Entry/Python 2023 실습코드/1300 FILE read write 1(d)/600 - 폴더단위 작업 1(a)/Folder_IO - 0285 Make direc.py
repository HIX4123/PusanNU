

import os


#print os.chdir('D:\\')  # 디렉토리를 옮김
#print glob.glob("*")


print("\n 여기는 어디인가 ===> ", end=' ')
print(os.getcwd( ))  # 나는 어디인가 ?


for x in range(10):
    dname= "test"+ str(x).zfill(4)
    print(dname)
    os.mkdir( dname )


allfiles = os.listdir('.')
print(allfiles)