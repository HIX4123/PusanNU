
myfile = open("mogi-dna-01.inp" ,"r")  # 읽을 파일을 준비 함
S=""

for oneline in myfile  :     # 한 라인씩 읽음
    myline = oneline.strip() # 마지막의 enter keY는 떼어내야 한다.
    S += myline


print(S)