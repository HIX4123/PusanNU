
# https://docs.python.org/2/tutorial/floatingpoint.html
# 숫자 0.1을 유한한 자릿수의 이진수로 나타낼 수 없다.



x = 0.1 + 0.1+ 0.1
y = 0.1+ 0.1+ 0.1+ 0.1+ 0.1+ 0.1
print("x= ", x)
print("y= ", y)

print("\n x(%%20.10f)= %20.10f" % x)
print("\n x(%%30.20f)= %30.20f" % x)
print("\n x(%%40.30f)= %40.30f" % x)
print("\n y(%%20.18f)= %20.8f" % y)