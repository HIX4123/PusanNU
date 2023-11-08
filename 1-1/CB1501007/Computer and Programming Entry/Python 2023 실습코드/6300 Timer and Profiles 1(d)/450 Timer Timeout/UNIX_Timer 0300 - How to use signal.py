#-------------------------------------------------------------------------------
# Purpose:     2020 컴퓨터및 프로그래밍 입문
# Author:      Cho
# Created:     2020-06-02
#-------------------------------------------------------------------------------

# signal을 이용하는 이 방법은 UNIX에서만 작동


import signal

def handler(signum, frame):
    print("마구 마구 찍어보자")
    raise Exception("종칩니다")


def loop_forever( ) :
    import time

    while( True ) :
        print("초")
        time.sleep(1) # 1초 쉬고


if __name__ == "__main__" :
    signal.signal( signal.SIGALRM, handler)
    signal.alarm(5)

    try:
        loop_forever( )
    except Exception as exc:
        print(exc)

