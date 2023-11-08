
with open("Wed_Child.txt") as f:
    this = f.read().splitlines()  # 전체를 읽어서 줄별로 list 원소에 담음


print (this)

for i, w in enumerate(this) :
    print (i, ": ", w)


f.close()