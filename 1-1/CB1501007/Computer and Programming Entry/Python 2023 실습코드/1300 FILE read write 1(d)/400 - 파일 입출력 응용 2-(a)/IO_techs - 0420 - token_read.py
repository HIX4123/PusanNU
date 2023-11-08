
# Problem Solving Class A
# 파일에 한 줄에 여러 개의 자료(token)이 있을 때
# 하나씩 token type으로 읽는 연습을 합니다.



print("------------단어별 읽기 --------------")
myfile = open("Stairway.txt" ,"r")  # 읽을 파일을 준비 함

for oneline in myfile  :     # 한 라인씩 읽음
    data = oneline.split()   # 읽은 라인을 리스트(List)로 만듬
    print("\n 라인  리스트 = ", data)

    for location  in range( len(data) ) :
        print(location+1, "= ", data[ location ])

myfile.close()  # 한번  연 화일은 반드시 닫아야만 됩니다.
                # 그래야만 수행 중 오류가 나지 않습니다.