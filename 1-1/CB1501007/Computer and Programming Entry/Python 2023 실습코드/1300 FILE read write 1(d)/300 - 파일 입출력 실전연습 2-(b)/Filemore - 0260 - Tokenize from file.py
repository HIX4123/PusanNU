# Problem Solving Class A
# 파일에 한 줄에 여러 개의 자료(token)이 있을 때
# 하나씩 token type으로 읽는 연습을 합니다.

Kdic={}
myfile = open("Tnews.txt" ,"r", encoding='cp949')  # 읽을 파일을 준비 함

i = 1
for oneline in myfile  :     # 한 라인씩 읽음
    myline = oneline.strip()
    tlist= myline.split()
    print (i, "라인= ", tlist)
    for w in tlist :
        if w in Kdic.keys():
            Kdic[w] += 1
        else :
            Kdic[w]=1
    i += 1

for w in Kdic.keys():
    print("w=", w, " ", Kdic[w] )

myfile.close()  # 한번  연 화일은 반드시 닫아야만 됩니다.
                # 그래야만 수행 중 오류가 나지 않습니다.