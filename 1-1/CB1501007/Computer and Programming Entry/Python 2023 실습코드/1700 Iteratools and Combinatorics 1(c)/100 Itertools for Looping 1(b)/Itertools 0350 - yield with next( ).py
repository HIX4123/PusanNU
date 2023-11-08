
## Example 3: Using generators
a,b = 0,1
def fibI():
 global a,b
 while True:
  a,b = b, a+b
  yield a        #필요할 때만 부르고 계산을 미룬다.

f=fibI()

print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))
