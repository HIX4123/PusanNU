
"""
바이너리 모드 파일을 다루기 위해 pickle 모듈을 사용한다.
pickle 모듈을 사용하면 파이썬에서 사용되는 객체를
바이너리 파일로 저장할 수 있다.
바이너리 파일을 쓰기 위해 dump 함수를,
읽기 위해 load 함수를 사용한다.
덤프(dump)한 순서대로 로드(load)된다.
"""

import pickle


number_of_data = int(input('Enter the number of data : '))
data = []

for i in range(number_of_data):
    raw = input('Enter data '+str(i)+' : ')
    data.append(raw)

file = open('./data/List_dump.bin', 'wb')

# dump and close
pickle.dump(data, file)
file.close()


