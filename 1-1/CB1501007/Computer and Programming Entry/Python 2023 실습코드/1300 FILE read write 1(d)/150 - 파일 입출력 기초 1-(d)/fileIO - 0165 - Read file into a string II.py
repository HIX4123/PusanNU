# 전체 파일을 하나의 문자열로 읽어 넣음

myfile = open('rotary.txt', 'r',encoding='cp949')

mystring   = myfile.read()
myfile.close()

print(f"\n 파일 문자열 \n\n {mystring}")
print(f"\n 문자열 길이 ={len(mystring)}")

myfile = open('rotary.txt', 'r',encoding='cp949')
yourstring = myfile.read().replace('\n', ' ')

print(f"\n 파일 문자열(\\n 삭제 후) \n\n {yourstring}")
print(f"\n 문자열 길이 ={len(yourstring)}")

myfile.close()