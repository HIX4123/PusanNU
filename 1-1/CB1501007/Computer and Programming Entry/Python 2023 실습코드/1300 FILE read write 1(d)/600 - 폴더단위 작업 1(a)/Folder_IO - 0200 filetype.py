
import os
import glob
import shutil

def filetype( fpath ) :
    print(fpath , ':', end=' ')
    if os.path.isfile( fpath) :
        print("정상적인 화일")
    if os.path.isdir( fpath) :
        print("정상적인 디렉토리")
    if os.path.islink( fpath) :
        print("심볼릭 링크, 링크화일")

myfiles =  glob.glob('*')
for x in myfiles :
    filetype( x )


#os.rename( 'sample.txt', 'another.txt') # 화일 이름을 바꾼다.
shutil.copyfile('sample.txt', '내가또복사함.txt')

#os.remove('*.tmp')  # tmp 화일을 모두 지워버린다.