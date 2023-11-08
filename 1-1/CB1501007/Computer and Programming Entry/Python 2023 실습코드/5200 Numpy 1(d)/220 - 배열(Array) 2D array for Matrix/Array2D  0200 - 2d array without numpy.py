
def printM( X):
    for A in X :
         print("\n")
         for b in A :
            print(b, end=' ')

n = 5
m = 6
a = [[0] * m] * n
a[0][0] = 25


printM(a)

# This can be easily seen if you set the value of
# a[0][0] to 5, and then print the value of a[1][0] ?
# it will also be equal to 5.
# The reason is, [0] * m returns just a reference to a list of
# m zeros, but not a list.
# The subsequent repeating of this element creates
# a list of n items that all reference to the same list
# (just as well as the operation b = a for lists does not create
# the new list), so all rows in the resulting list are actually
# the same string.


m = 4
b = [0] * n
for i in range(n):
    b[i] = [0] * m

b[0][0]= 33
printM(b)

