# Problem Solving Class A
# 파일에 한 줄에 여러 개의 자료(token)이 있을 때
# 리스트 원소로 읽습니다.
# 단 \n을 하나의 문장으로 인식합니다.
# 읽을 파일을 준비 함

f = open("mother-sister.txt", "r" , encoding='cp949')


line = f.readline()

i = 1

while line:
    print(i, " = ", line.strip())  #line.strip( )은 line의 끝에 있는 \n을 제거하는 작업
    line = f.readline()
    i = i +1

f.close()

