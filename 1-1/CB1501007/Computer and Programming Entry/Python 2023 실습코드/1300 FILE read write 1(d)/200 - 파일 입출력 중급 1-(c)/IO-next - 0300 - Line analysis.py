# Problem Solving Class A
# 파일에 한 줄에 여러 개의 자료(token)이 있을 때
# 리스트 원소로 읽습니다.
# 단 \n을 하나의 문장으로 인식합니다.
# 읽을 파일을 준비 함




fh =  open("mother-sister.txt", "r")

for line in fh:
    buffer = line.split()
    #print(buffer)
    for w in buffer :
        if "는" in w :
            print(w)




fh.close()
