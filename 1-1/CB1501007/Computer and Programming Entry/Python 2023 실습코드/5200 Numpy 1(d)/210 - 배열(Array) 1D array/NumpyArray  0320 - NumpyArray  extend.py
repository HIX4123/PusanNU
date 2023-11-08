
import array

a = array.array('i', range(5))
print('Initial :', a)

a.extend(range(5))
print('Extended:', a)

print('Slice   :', a[3:6])

print('Iterator:', list(enumerate(a)))
