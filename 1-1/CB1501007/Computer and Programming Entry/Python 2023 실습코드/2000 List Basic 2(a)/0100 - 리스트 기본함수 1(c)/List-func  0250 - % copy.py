
# List에서 Copy를 할 때는 매우 유의해야 한다.

la = [ 'burger', 'cola', 'ketchup', 'coffee', 'chicken']
lb = la

print("Original")
print("la = ", la)
print("lb = ", lb)
la.pop(3)
print("\n after la.pop(3)")
print("la = ", la)
print("lb = ", lb)

x = 100
y = x
print(x, y)
y += 1
print("y값을 1 증가시킨 후의 값의 변화")
print("x = %d, y= %d " % (x,y))


