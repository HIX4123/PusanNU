

#fname = input("만들고 싶은 파일의 이름 *.txt: ")


myfile = open( "dragon.txt", "w")  # open( )준비
print("착하게 살자")
print("착하게 살자", file=myfile)
print("인간들아 정말 착하게 살자", file=myfile)
print("교수님 말 잘 듣고", file=myfile)
print("하나 둘 셋 넷 10까지 적어보자.", file=myfile)

for w in range(10):
    print( w, file=myfile)


myfile.close()         # 이것이 없으면 화일이 저장이 안됩니다. 끝내기 작업
