#-------------------------------------------------------------------------------
# Purpose:     2020 컴퓨터및 프로그래밍 입문
# Author:      Cho
# Created:     2020-06-02
#-------------------------------------------------------------------------------

from functools import wraps
import errno
import os
import signal

class TimeoutError(Exception):
    pass

def timeout(seconds=10, error_message=os.strerror(errno.ETIME)):
    def decorator(func):
        def _handle_timeout(signum, frame):
            raise TimeoutError(error_message)

        def wrapper(*args, **kwargs):
            signal.signal(signal.SIGALRM, _handle_timeout)
            signal.setitimer(signal.ITIMER_REAL,seconds) #used timer instead of alarm
            try:
                result = func(*args, **kwargs)
            finally:
                signal.alarm(0)
            return result
        return wraps(func)(wrapper)
    return decorator


# 여기서 부턴 개인적인 testing함수
@timeout(2)
def testing():
    import time
    count = 0
    while count < 3:
        print('helloworld', count)
        count += 1
        time.sleep(1)
    return count


# 위에 나온 부분이 어디서든 검색해보면 볼 수 있는 timeout decorator를
# 만드는 방법이다. testing이라는 특정함수를 2초 안에 실행되지 못하면
# 5회 다시 시도할 것이고, 그래도 안되면 이후 모션들을 취할 예정이다.

count = 0


while count < 5:
    try:
        testing()
        break
    except Exception as e:
        print('timeout occur: ', str(e), count)
        count += 1


