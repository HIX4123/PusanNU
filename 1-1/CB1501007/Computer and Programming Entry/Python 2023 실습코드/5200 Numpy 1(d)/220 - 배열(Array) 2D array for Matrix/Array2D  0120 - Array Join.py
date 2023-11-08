
a = [[17, 27, 37], [45, 55, 65]]
print((a[0]))
print((a[1]))
b = a[0]
print(b)
print((a[0][2]))
a[0][1] = 7
print(a)
print(b)
b[2] = 9
print((a[0]))
print(b)


a = [[1, 2, 3, 4], [5, 6], [7, 8, 9]]
for i in range(len(a)):
    for j in range(len(a[i])):
        print(a[i][j], ' ', end=' ')


print("\n Join operation \n")
for row in a:
    print(' '.join([str(elem) for elem in row]))