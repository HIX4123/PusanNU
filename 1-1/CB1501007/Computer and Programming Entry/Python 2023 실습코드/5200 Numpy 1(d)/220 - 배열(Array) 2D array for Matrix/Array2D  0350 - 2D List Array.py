
a = [[ [] for y in range(8)] for x in range(8)]

a[3][4].append(5)
a[4][5].append("Summer")
a[7][7].append("Winter")
a[7][7].append("X-man")
print("One element=", a[1])
print("One element=", a[3])


print("Matrix=", a)
