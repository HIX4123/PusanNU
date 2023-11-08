"""
전체 각 줄로 나누어진 파일을 한번에 읽어
중간 enter key를 모두 지운 다음
하나의 문자열로 만드는 방법

key는 file.read( )를 사용하여 전체를
통으로, 하나의 문자열로 읽는 것.
"""

# writedata.py
f = open("dna0.txt", 'r',encoding='cp949')


mydata = f.read( )
print("mydata>>\n", mydata)
print("길이는 = ",  len(mydata))
print("my data의 유형은 ",  type(mydata) )
print(" enter key의 수= ",  mydata.count("\n") )

multiline = mydata.split()
oneline = ''.join( multiline ) # 하나로 합침
print("\n oneline = ", len(oneline)) # print에서 ',' 다음에는 default로 공백 1개
print(oneline,"$" )

print("다른 방법, enter key를 삭제하는 방법 : \n")

oneline2 = mydata.replace("\n","")
print(oneline2a=)

f.close()