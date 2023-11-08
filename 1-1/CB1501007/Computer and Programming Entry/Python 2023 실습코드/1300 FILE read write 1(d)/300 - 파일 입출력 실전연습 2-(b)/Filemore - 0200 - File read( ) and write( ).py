# Problem Solving Class A
# 파일에 한 줄에 여러 개의 자료(token)이 있을 때
# 하나씩 token type으로 읽는 연습을 합니다.


inpf  = open("mother-sister.txt" ,"r", encoding='cp949')  # 읽을 파일을 준비 함
outf  = open("new.txt", "w")  # 쓸 화일을 준비 함

wget = inpf.read( )
print(wget)


word = "One summer night!"
outf.write(word)

inpf.close()
outf.close()