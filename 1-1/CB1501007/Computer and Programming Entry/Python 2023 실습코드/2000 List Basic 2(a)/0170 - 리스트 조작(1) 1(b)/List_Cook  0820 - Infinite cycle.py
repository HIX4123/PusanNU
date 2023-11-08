
from itertools import cycle

count = 0
for p in cycle([1,2,3]):
  print("endless cycle:", p)
  count += 1
  if count > 100 : break