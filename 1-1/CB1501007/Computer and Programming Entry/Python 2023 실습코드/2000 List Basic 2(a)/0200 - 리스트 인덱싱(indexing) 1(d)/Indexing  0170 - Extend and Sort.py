# List에 응용할 수 있는 방법

dlist = ['spam', 1, ['Brie', 'Roquefort', 'Pol le Veq'], [1, 2, 3]]

a = [1, 2, 3]
b = [4, 5, 6]
c = a + b
print("\n실험 100\n")
print(c)
print([0] * 4)
print([1, 2, 3] * 3)


t = ['a', 'b', 'c', 'd', 'e', 'f']
print("exp-01", t[1:3])
print(t[:4], t[3:])

t = ['a', 'b', 'c']
t.append('d')
print("exp-02", t)

# 리스트 적용할 수 있는 method()
# 쌀.밥하기()
# 사과.깍기()  사과.밥하기() ??

t1 = ['a', 'b', 'c']
t2 = ['d', 'e']
t1.extend(t2)
print("exp-03", t1)

t = ['d', 'c', 'e', 'b', 'a']
t.sort()
print("exp-04", t)


# Built-In function
t = [1, 2, 3]
print("exp-05", sum(t))




