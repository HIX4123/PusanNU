# 파일에 한 줄에 여러 개의 자료(token)이 있을 때
# 하나씩 token type으로 읽는 연습을 합니다.


filestring = open("mother-sister.txt" ,"r",   encoding='cp949').read()  # 읽을 파일을 준비 함

print( "whole String=", filestring   ,"\n\n")

# You can even make a list with it!
sstring = filestring.split('\n')

for i,x in enumerate(sstring) :
    print (i, "=", x)