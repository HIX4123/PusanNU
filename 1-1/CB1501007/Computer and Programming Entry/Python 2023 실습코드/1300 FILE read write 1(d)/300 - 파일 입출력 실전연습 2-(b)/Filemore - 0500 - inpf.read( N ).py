# 파일에 한 줄에 여러 개의 자료(token)이 있을 때
# 하나씩 token type으로 읽는 연습을 합니다.


inpf  = open("mother-sister.txt" ,"r",   encoding='cp949')  # 읽을 파일을 준비 함

N = 20
wget = inpf.read( N  )
print ("batch 1= ", wget, len(wget))

N = 10
wget = inpf.read( N  )
print ("batch 2= ", wget   , len(wget))


inpf  = open("LineText.txt" ,"r",   encoding='cp949')  # 읽을 파일을 준비 함

N = 20
wget = inpf.read( N  )
print ("batch 1= ", wget, "\n: length=", len(wget))

N = 10
wget = inpf.read( N  )
print ("batch 2= ", wget   , "\n: length=", len(wget))

inpf.close()
