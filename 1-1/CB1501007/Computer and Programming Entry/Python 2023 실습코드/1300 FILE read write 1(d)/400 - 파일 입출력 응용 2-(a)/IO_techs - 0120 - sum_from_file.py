
myfile = open("numfile.txt", "r")
isum = 0

while ( True ) :
    token = myfile.readline()
    if token == "" : break  # 읽은 줄이 화일의 마지막인 경우
    else : # 정상적인 문자열인 경우
        itoken = int (token) # 문자를 정수로 바꿉니다.
        print(itoken, end=' ')
        isum += itoken

print("\n 전체 합계는 = ", isum)
myfile.close()




