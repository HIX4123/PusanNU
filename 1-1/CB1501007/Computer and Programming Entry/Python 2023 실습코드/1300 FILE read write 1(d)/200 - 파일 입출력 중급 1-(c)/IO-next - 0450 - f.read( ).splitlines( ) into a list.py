# 영어는 cp949로 읽을 필요가 없다. 그러나 사용해도 무방하다.
#

with open("Wed_Child.txt", encoding='cp949') as f:
    this = f.read().splitlines()


print (this)

for i, w in enumerate(this) :
    print (i, ": ", w)


f.close()