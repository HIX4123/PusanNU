
# 지정한 화일에서 단어(token)을 읽어서 그것을 분석하는 프로그램입니다.

#-------------------- 실험 2 -------------#
myfile = open("name.inp", "r")   # r로 파일을 읽습니다. read
# myfile = open("name.inp")
line = myfile.readline()

while line:                      # 계속 작업을 수행한다.
    iniName = line[0:2]          # 이름 첫 글자 저장 (한글은 2byte이므로 0~2번 데이터를 가져와야 합니다.)
    if (iniName == '김'):        # 첫 글자(성)이 '김' 씨인 사람만 출력합니다.
        print(line)
    line = myfile.readline()    # 다음 줄 읽기

print("모든 작업을 종료 합니다.")

myfile.close()  # 반드시 닫아야 합니다.
