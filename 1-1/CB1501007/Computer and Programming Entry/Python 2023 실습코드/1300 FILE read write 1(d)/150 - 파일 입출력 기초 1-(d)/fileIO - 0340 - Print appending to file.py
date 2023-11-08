
#myfile = open("test-01.out", "a")   # 축적 logging 쌓을때
myfile = open("test-01.out", "w",encoding='cp949')

print ("1. 김치국밥 6000", file=myfile)
print ("2. 피자 5600", file=myfile)
print ("3. 라면 1900", file=myfile)
print ("4. 된장찌개 5300", file=myfile)
print ("5. 살아있네. 쥑이네...", file=myfile)

myfile.close();

