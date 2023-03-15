# 이것은 설명문(comment)입니다.


a = 800
print(f"1> a= {a},  id(a)={id(a)}")

a = a + 10
print(f"2> a= {a},  id(a)={id(a)}")

a = a
print(f"3> a= {a},  id(a)={id(a)}")

b = a
print(f"4> b= {b},  id(b)={id(b)}")

b = b - a
print(f"5> a= {a},  id(a)={id(a)}")
print(f"6> b= {b},  id(b)={id(b)}")

b = 810
print(f"7> a= {a},  id(a)={id(a)}")
print(f"8> b= {b},  id(b)={id(b)}")