
# N개의 박스에 N-1개의 black ball과 1개의 red ball이 있다.
# 두 사람이 번갈아가며 볼을 가져갈 때 red는 집어가는 사람이 이긴다.

import random
select= [0]*20
select.append(1)
random.shuffle(select)
print(select)


for i,x in enumerate(select) :
    if x == 1 :
        if (i+1)%2 == 1 :
            print("First Wins!")
        else :
            print("Second Wins!")


# So if '1' occupies in the even position of List
# then seconds Win.
