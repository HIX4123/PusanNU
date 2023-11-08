
myl = ['a', 'e', 'i', 'o', 'u' ]

c = input("하나의 소문자를 입력하세요:")

if c not in myl :  print(c, " 는 자음입니다")
else :  print(c, " 는 모음입니다.")


print("\n 다르게 비교해도 ")
if c in myl :  print(c, " 는 모음입니다")
else :  print(c, " 는 자음입니다.")
