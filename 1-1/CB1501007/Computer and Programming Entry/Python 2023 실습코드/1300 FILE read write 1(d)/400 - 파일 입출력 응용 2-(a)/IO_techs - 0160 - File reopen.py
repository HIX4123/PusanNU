
# Problem Solving Class A
# 파일에 한 줄에 여러 개의 자료(token)이 있을 때
# 하나씩 token type으로 읽는 연습을 합니다.


in_file  = open("Stairway.txt" ,"r" ,   encoding='cp949')  # 읽을 파일을 준비 함

for aline in in_file :
    print("==>", aline.strip())  # 라인 끝의 \n을 떼낸다. 끝

in_file.seek(0)   # file pointer를 처음으로 되돌린다. re-open()
aline  = in_file.readline()

while aline :
    print("--> ", aline.strip())
    aline  = in_file.readline()

in_file.close()
