
# 특정 수 R의 배수를 출력합니다.


count = 0
R = 77

while (True) :
    if count > 500 : break
    if count% R == 0 :
        print(count)

    count += 1



st = "This is an example statement. Is it a good?"
vowel = [ "a", "e", 'i', 'o', 'u']
i=0
while( i < len(st)):
    if st[i] in vowel :
        print((i, "문자", st[i]))
    i += 1



