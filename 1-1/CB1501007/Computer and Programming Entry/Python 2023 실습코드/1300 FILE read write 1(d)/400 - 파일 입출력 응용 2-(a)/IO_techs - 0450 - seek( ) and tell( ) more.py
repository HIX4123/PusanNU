
# Problem Solving Class A
# 파일에 한 줄에 여러 개의 자료(token)이 있을 때
# 하나씩 token type으로 읽는 연습을 합니다.


fname = "rainyday.txt"
f  = open( fname ,"w+")  # w+ 읽고 쓰기로 파일을 준비 함

s = "Oh! My God"
t = "DONOT HATE ME. PLEASE forgive them"

# f.seek(k) 파일의 처음 위치에서 앞으로 k 바이트 전진
# f.seek(k,1) 현재 위치에서 앞으로 k 바이트 전진
# f.seek(k,2) 뒤에서 k바이트 후진, k는 보통 음수

f.seek(20)  # move forward +20
f.write(t)

print("The current position ", f.tell())

f.seek(-13,2)  # 뒤에서 3번째
f.write(s)

f.close()
