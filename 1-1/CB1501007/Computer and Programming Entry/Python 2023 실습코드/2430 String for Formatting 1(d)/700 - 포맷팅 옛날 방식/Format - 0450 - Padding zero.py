
n = '4'
print(n.zfill(10))


n = 4
print('%03d' % n)
print(format(n, '03')) # python >= 2.6
print('{0:03d}'.format(n))  # python >= 2.6
print('{foo:03d}'.format(foo=n))  # python >= 2.6
print(('{:03d}'.format(n)))  # python >= 2.7 + python3
print(('{0:03d}'.format(n)))  # python 3


print("ljust 와 rjust")
t = 'test'
print(t.rjust(10, '0'))
print(t.ljust(10, '0'))


n = 3
print("Type 1", str(n).zfill(5))
n = '3'
print("Type 2", str(n).zfill(5))
n = '3.0'
print("Type 3", str(n).zfill(5))


width = 10
x = 5
print("가장 간단한 방법:", "%0*d" % (width, x))

