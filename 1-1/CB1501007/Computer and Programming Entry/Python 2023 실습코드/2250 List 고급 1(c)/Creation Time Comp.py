
def initAndWrite():
  x = [None]*10000
  for i in range(10000):
      x[i] = i

def initAndWrite2():
  x = [None for _ in range(10000)]
  for i in range(10000):
   x[i] = i

def appendWrite():
  x = []
  for i in range(10000):
   x.append(i)

import timeit
for f in [initAndWrite, initAndWrite2, appendWrite]:
    etime = timeit.timeit(f, number=1000)*1000
    print(etime)
    print(('{} takes {} usec/loop'.format(f.__name__, timeit.timeit(f, number=1000)*1000)))

