import os


path = './data' # 현재 이 py code가 있는 위치


obj = os.scandir()


print( f' 화일과 폴더 in {path}')


for entry in obj :
    if entry.is_file():
        if entry.name[-3:]== r'.py' :  # xpy
            print(entry.name)



# entry.is_file() 는 entry가 file인지 아닌지를 확인
# entry.is_dir() : directory인지의 여부를 확인


# iterator and # free acquired resources는 반드시 닫아야 함.
obj.close()


