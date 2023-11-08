

myfood =  ["짜장면", "탕수육", "잡채밥", "김밥", "우동", "스파게티", "콩밥"]
yourfood = ["떡",     "커피",   "사탕",   "홍차", "단술", "오뎅"  ]
month = [ 45, 56, 11, 23, 90, 678, 'kill']
print((len(month)))

for idx, x in enumerate(month) :
    print(("[", idx, "]번째 원소는 [", x  , "] 입니다."))


print("\n format string을 이용한 멋진 출력문 만들기")
for idx, x in enumerate(month) :
    print(("[ %d 번째 원소 ===>>> %s ㅋㅋㅋㅋ " % (idx,x)))

# %d는 정수에 대응 %s는 문자열을 찍을 때 대응함

print("\n 쌍으로 묶어서 looping하기 ")
for my , your in zip(myfood, yourfood) :
    print((my, your))


print("\n 리스트의 역순으로 뽑아내기 ")
for my in reversed(myfood) :
    print(my)



print("\n 리스트의 새로 정렬해서 빠른 순으로 뽑아내기 ")
for my in sorted(myfood) :
    print(my)
