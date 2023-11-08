# 앞과는 다르게 1차 함수 f(x)의 계수를 tuple로 활용하는 방법


from numpy.polynomial import polynomial as P

f = (1,1,1,1,1,1)  # 1 + x + x^2 ... x^5
g = (-1,1)         # 1 - x

print(" f(x)+g(x) = :", end=" ")
print(P.polyadd(f,g))
print(" f(x)-g(x) = :", end=" ")
print(P.polysub(f,g))
print(" f(x)*g(x) = :", end=" ")
print(P.polymul(f,g))
print(" f(x)/g(x) = :", end=" ")
print(P.polydiv(f,g))

# it is difficult!.
# it is challenging !
