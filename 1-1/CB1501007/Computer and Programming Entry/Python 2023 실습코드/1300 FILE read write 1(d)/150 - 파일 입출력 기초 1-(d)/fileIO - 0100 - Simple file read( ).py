
myfile = open("Cambia.txt", "r",encoding='cp949')
i= 1

while True:
    line = myfile.readline()
    if( line == '') :       # 마지막 줄의 검사. 반드시 뒷줄에 빈 return문자
        print(" 입력 파일의 끝에 도달: 모두 다 읽었습니다.")
        break   #While Loop을 빠져 나간다. break the while Loop
    else:
        print(f" {i:2}-> {line.strip()}" )  # >strip( )은 마지막 \n을 삭제함
        i=i+1

myfile.close()

myfile = open("Cambia.txt", "r")
i= 1
print("\n\n Token으로 나누어 읽기")
while True:
    line = myfile.readline()
    if( line == '') :       # 마지막 줄의 검사. 반드시 뒷줄에 빈 return문자
        print(" 입력 파일의 끝에 도달: 모두 다 읽었습니다.")
        break   #While Loop을 빠져 나간다. break the while Loop
    else:
        print(f" {i:2}-> {line.split( )}" )
        i=i+1

myfile.close()
