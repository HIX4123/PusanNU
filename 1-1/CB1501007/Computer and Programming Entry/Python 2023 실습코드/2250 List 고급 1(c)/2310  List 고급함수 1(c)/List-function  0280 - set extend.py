

a = { 1, 2, 3, 4, 5}

print(a)
a.add("111")
print(a)
a.add( 9 )
print(a)


x = set(["Postcard", "Radio", "Box", "Telegram", "Crying"])
x.remove("Box")
print("1=", x)
y = set(["Radio","Television"])
print("2=",  x.difference(y))
print("3=",  y.difference(x))