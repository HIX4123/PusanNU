
# ㄱ ~ ㅎ: 0x3131 ~ 0x314e
# ㅏ ~ ㅣ: 0x314f ~ 0x3163
# 가 ~ 힣: 0xac00 ~ 0xd79f
import string

def take_korean(S):
    lu = ""
    for x in list(S) :
        if x not in string.printable :
            #print x
            lu += x
    return( lu )


ks =  "du용mm한글+-흥 호유가 노니다 이ㄴ다   ㅎㅎㅎutg/-"
us = "du용mm한글+-이ㄴ다   ㅎㅎㅎutg/-"


print("1=", take_korean(ks))
print("2=", take_korean(us))


c = "밀"
print(c)
c = "밀".encode('utf-8')
print(list(c))

lx= [  "동" , "ㅠㅠㅠ",  "ㅂㅂㅂ", "명", "책상", "바다", "몸", "ㅋㅋㅋ" ]

print("\n 한글 글자 단위 범위 실험")
for i,w in enumerate(lx) :
    if "가" <= w <= "힝" :
        print(i, "=", w, "IN")
    else :
        print(i, "=", w, "OUT")

print("\n 한글 모음 범위 실험")
for i,w in enumerate(lx) :
    if "ㅏ" <= w <= "ㅣ" :
        print(i, "=",w, "IN")
    else :
        print(i, "=",w, "OUT")

print("\n 한글 자음 범위 실험")
for i,w in enumerate(lx) :
    if "ㄱ" <= w <= "ㅎ" :
          print(i, "=",w, "IN")
    else :
        print(i, "=",w, "OUT")


print("\n 문자열에서 자모 추출 실험")
lks = list(ks)
for i,c in enumerate(lks) :
    print(i, "=", c)  # 단일 자모와 한글자의 초성과는 다르다.
    if "ㄱ" <= c <= "ㅎ" :  print(i, "=", c, "IN")
