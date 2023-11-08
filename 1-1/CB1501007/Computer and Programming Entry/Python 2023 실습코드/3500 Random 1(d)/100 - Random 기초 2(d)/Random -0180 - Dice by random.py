
import random   # for random
random.seed()   # 씨앗(seed)값 설정하기. 시간 정보에 의해 초기화됨

# 가상 주사위 함수
def virtual_dice():
    return random.randrange(1, 7)   # 1~6 사이의 정수를 랜덤으로 생성하여 반환

# 윳 함수
def yut():
    pan= [ '도', '개', '걸', '윷', '모']
    return   random.choice(pan)                       # 채워넣으시기 바랍니다


for k in range(10):
    print(random.random())           # 0~1 사이의 실수를 랜덤으로 생성하여 출력

for k in range(10):
    print(random.randrange(100))     # 0~100 사이의 정수를 랜덤으로 생성하여 출력

# 주사위 100번 굴리기
for k in range(20):
    print(virtual_dice() , yut())            # virtual_dice() 함수를 호출하여 반환된 값을 출력
