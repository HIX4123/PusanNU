
from itertools import cycle

count = 0
for p in cycle( list("월화수목금토일")):
  print(f" day={count}, {p}")
  count += 1
  if count > 100 : break