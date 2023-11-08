

myfile = open("Wed_Child.txt" ,"r")  # 읽기모드로 열어 둡니다.
this = myfile.readlines()   # readlines( )는 전체를 읽어 \n 기준으로 List를 만듬.

print("문장의 수는 = ", len(this))
for i, w in enumerate(this) :
    myline = w.strip()
    myword = myline.split()
    print(i, ":", myword )

myfile.close()  # 연 파일은 반드시 닫아야 합니다..