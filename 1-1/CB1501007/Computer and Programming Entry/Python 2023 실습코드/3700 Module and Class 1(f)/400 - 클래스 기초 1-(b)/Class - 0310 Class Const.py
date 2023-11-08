
from time import time, ctime, sleep

class Life:
    def __init__(self):         # 생성자
        self.birth = ctime(time())
        print(('생성시간= ', self.birth))
    def __del__(self):          # 파괴자
        print(('파괴시간= ', ctime(time())))

def test():
    mylife = Life()
    print('Sleeping for 3 sec')
    sleep(3)    # 3초가 쉬는 작업

test()
