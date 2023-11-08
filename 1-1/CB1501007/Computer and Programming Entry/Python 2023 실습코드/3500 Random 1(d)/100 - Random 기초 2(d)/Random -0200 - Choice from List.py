

import random
myl=range(1,21)

print("\n\n 샘플링, 20개 중에서 5개 중복허용 선택하기 ")
for x in range(10):
    val = [random.choice(myl) for i in range(5)]
    print("중복허용 샘플링 = ", val)


