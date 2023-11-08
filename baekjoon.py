x, y = map(int, input().split())
dif, day = y - x, 0
for i in range(1, 2 ** 31):
    for _ in range(2):
        if dif <= 0:
          print(day)
          exit()
        day += 1
        dif -= i