# 이것은 설명문(comment)입니다.


a = [1,2,3,4,5]
b = a
print(f"\n")
print(f"> a= {a},  id(a)={id(a)}")
print(f"> b= {b},  id(b)={id(b)}")

c = [1,2,3,4,5]
print(f"> c= {c},  id(c)={id(c)}")  # 리스트는 숫자와 달리 같아도 다른 id를 가진다.

b.append(0)
print(f"\n")
print(f"> a= {a},  id(a)={id(a)}")
print(f"> b= {b},  id(b)={id(b)}")
print(f"> c= {c},  id(c)={id(c)}")





