
for x in range(10):
    for y in range(10):
        for z in range(10):  # for z
            print((x,y,z))
            if x*y*z == 30:
                break # for z loop을 벗어나서 17번 라인
        else:
            continue
        break
    else:             # 17
        continue
    break             # 다시 Break