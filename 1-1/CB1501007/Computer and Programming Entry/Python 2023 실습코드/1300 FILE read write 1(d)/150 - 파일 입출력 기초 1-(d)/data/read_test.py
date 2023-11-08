# Problem Solving Class A
# 파일에 한 줄에 여러 개의 자료(token)이 있을 때
# 리스트 원소로 읽습니다.
# 단 \n을 하나의 문장으로 인식합니다.
# 읽을 파일을 준비 함

myfile = open("Cambia.txt", "r")
i= 1

while True:                        # 계속 작업을 수행한다.
    line = myfile.readline()
    if( line == '') :       # 마지막 줄의 검사. 반드시 뒷줄에 빈 return문자
        print(" 입력 파일의 끝에 도달: 모두 다 읽었습니다.")
        break   #While Loop을 빠져 나간다. break the while Loop
    else:
        print(i, "->", (line))
        i=i+1


myfile.close()
