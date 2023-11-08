# 파일에 한 줄에 여러 개의 자료(token)이 있을 때
# 하나씩 token type으로 읽는 연습을 합니다.


myfile = open("mother-sister.txt" ,"r")  # 읽을 파일을 준비 함

i = 1
S=""
for oneline in myfile  :     # 한 라인씩 읽음
    myline = oneline.strip()
    S += myline
    print( i, "라인= ", myline)
    i += 1


LS =  len(S)
print ("\n 길이=", LS ,"\n",  S)
print ("\n 전체 입력 Line" , S)

myfile.close()  # 한번  연 화일은 반드시 닫아야만 됩니다.
                # 그래야만 수행 중 오류가 나지 않습니다.