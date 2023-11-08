# 정해진 시간 간격으로 뭔가 작업을 해야 할 떄
# 모니터링
# 데이터 긁어오기 (주식, 예)


import time
import threading
N= 500
ct = 0

def thread_run( ):
    print(f' time= {time.ctime()}')
    for i in range(1,N+1):
        mywork() #원하는 작업
        print(f' Thread running')

    threading.Timer(2.5, thread_run) # 2.5초 간격으로 실행


def mywork( ):
    global ct
    ct += 1
    print("In my work() ", ct)
    return

thread_run( )