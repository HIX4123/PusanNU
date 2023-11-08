

import random


a= 10 ; b=20
print("\n\n 일양(uniform) 분포")
for x in range(10):
    val = random.uniform(a, b)
    print("uniform(a, b)=", val)

print("\n\n 표준정규분포")
for x in range(10):
    val = random.gauss(173.8, 5.9) # 평균이 173이고 분산이 3.5인 사람 키
    print("random.gauss(173.8, 5.9)=", val)

myl=["book", "note", "pen", "water", "USB", "card", "Phone", "Backpack", "bicycle", "Box"]
print("\n\n 샘플링, 20개 중에서 5개 중복없이 선택하기 ")
for x in range(10):
    val = random.sample( myl, 5)
    print("중복없이 샘플링 = ", val)



print("\n\n 샘플링, 20개 중에서 5개 중복허용 선택하기 ")
for x in range(10):
    val = [random.choice(myl) for i in range(5)]
    print("중복허용 샘플링 = ", val)


