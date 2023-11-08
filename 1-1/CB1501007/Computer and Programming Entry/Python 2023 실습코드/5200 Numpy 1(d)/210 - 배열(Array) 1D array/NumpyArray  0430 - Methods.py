
# append()
# extend()
# index()
# insert() pop() remove() reverse() fromlist()
# fromfile() tolist() tofile() tostring()

from array import *

a=array('i',[2,3,4,5])
print("result 1= ", a)

array('i', [2, 3, 4, 5])
a.insert(0,1)
print("result 2= ", a)

array('i', [1, 2, 3, 4, 5])
a.append(6)
print("result 3= ", a)

array('i', [1, 2, 3, 4, 5, 6])
b=array('i',[7,8,9])
a.extend(b)
print("result 4= ", a)

array('i', [1, 2, 3, 4, 5, 6, 7, 8, 9])
c=[2,4,6]

a.fromlist(c)
print("result 5= ", a)


