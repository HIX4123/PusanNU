
import random   # for random
random.seed( )  # 씨앗(seed)값 설정하기. 시간 정보에 의해 초기화됨

# 윳 함수
def stick():
    if random.random() < 0.45 : return(1)
    else : return (0)                   # 오픈된 것의 갯수

def call_yut( ) :
    sum = stick() + stick() + stick() + stick()
    if sum == 4 : return ("윷")
    if sum == 3 : return ("걸")
    if sum == 2 : return ("개")
    if sum == 1 : return ("또")
    else : return ("모")

print("윷을 10번 던집니다.")
for mal in range(10):
    print(call_yut( ))