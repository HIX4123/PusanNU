
i=1
while( i < 10):
    j=1
    print("\n-----", i, "단 ------")
    while (j < 10):
        print(i,"x", j, "=", i*j)
        j += 1

    i += 1


# 또 다른 표현

for x in range(10, 20):
    print("\n-------- ", x , "단 시작합니다. --------")
    for y in range(10, 20):
          print(x,y, "=", x*y)
