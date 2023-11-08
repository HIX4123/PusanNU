
# Lazy evaluation 즉 계산 결과 값이 필요할 때까지 계산을 늦추는 효과를 볼 수 있다.
# 위 sleep_func() 함수는 1초간 sleep 을 수행한 후 x 값을 return 하는 함수이다.
import time

def sleep_func(x):
    print("sleep...")
    time.sleep(0.5)
    return str(x)+"-- "

list = [ sleep_func(x) for x in range(5)]
# sleep_func( )을 바로 실행한다.

for i in list:  #미라 list를 다 계산해서 만들어 둔다. #이 과정에서 sleep...을 출력
    print(i)

# generator 생성
gen = (sleep_func(x) for x in range(5))

for i in gen:  #하나를 부르면 하나면 계산해서 출력한다.
    print(i)





