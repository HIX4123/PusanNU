
a = [1,2,3,4,5]
c = b = a

print("\nState 1 =")
print("a=", a)
print("b=", b)

b.append(-99)
print("\nState 2 =")
print("a=", a)
print("b=", b)

a.pop(0)
print("\nState 3 =")
print("a=", a)
print("b=", b)


a = ["New", "One"]  # 새로 assign하면 그 때 분리
print("\nState 4 =")
print("a=", a)
print("b=", b)
print("c=", c)

c= "Summer Time Killer"
print("\nState 5 =")
print("a=", a)
print("b=", b)
print("c=", c)
