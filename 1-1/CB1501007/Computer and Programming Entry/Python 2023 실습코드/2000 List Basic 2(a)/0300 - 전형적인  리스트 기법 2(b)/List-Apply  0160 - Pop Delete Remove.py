#-------------------------------------------------------------------------------

# List에서 원소 제거하는 함수 pop(), delete(), remove()

maxi = 78.90
t = ['a', 'b', 'c', 345, ["Good"],  "Kol", 456, (45 < 67), maxi ]
print("Origin List ", t)
x = t.pop(1)
print("After pop(1): " ,  x,t)
del t[3]
print("After t[3]: " ,t)
t.remove('Kol')
print("After remove -Kol-: " ,t)
