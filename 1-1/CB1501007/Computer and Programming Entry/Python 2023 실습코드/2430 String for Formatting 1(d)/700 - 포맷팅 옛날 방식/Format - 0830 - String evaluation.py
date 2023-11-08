
myfunc = open("funcstr.txt", "r")
fline = myfunc.readline().strip()

print("input line = ", fline)

x = 0.5  # 시작점

for m in range(10) :
    x = x + 0.1
    val = eval( fline )
    print(x, val)


myfunc.close()

