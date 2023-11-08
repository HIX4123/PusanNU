
# 어떤 문자열을 받아서 이것을 프로그램의 일부로 사용할 수 있습니다.

myfunc = open("funcstr.txt", "r")    # x**3 - 4*x**2 + 7*x - 1


fline = myfunc.readline().strip()

print("input line = ", fline)

x = 0.5  # 시작점

for m in range(10) :
    x = x + 0.1
    val = eval( fline )
    print(x, val)


myfunc.close()

