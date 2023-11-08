
s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9])

x =  s1 & s2
y =  s1 | s2
print("x= ", x)
print("y= ", y)

print("s1 - s2= ", s1 - s2)
print("s2 - s1= ", s2 - s1)
# Error: print "s1 + s2= ", s1 + s2


z = s1.intersection(s2)

print("s1= ", s1)
print("s2= ", s2)
print("z=  ", z)

z = s1.union(s2)
print("s1= ", s1)
print("s2= ", s2)
print("z=  ", z)

s1.update( s2 )
print("w1= ", s1)
print("w2= ", s2)

s1.remove(9)
print("w1.remove(9)= ", s1)


