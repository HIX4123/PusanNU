
squares = [x**2 for x in range(10)]
print(("실험 01:", squares))

la  = [i * i   for i in range(10)   if i % 2 == 0]
print(("실험 02:", la))


lc = [x.lower() for x in ["A","B","C"]]
ld = [x.upper() for x in ["a","b","c"]]

string = "Hello 12345 World"
le = [x for x in string if x.isdigit()]

print(lc)
print(ld)
print(le)
