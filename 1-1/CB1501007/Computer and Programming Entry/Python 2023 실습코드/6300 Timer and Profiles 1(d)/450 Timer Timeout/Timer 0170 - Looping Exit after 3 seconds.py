#-------------------------------------------------------------------------------
# Purpose:     2020 컴퓨터및 프로그래밍 입문
# Author:      Cho
# Created:     2020-06-02
#-------------------------------------------------------------------------------

from threading import Thread, Event
import time



stop_event  = Event() # Event 객체를 사용. Thread로 넘겨 줌
stop_event2 = Event()

def do_actions(): # 숫자를 출력하고 1초를 기다린 뒤에 return:
    i = 0
    while True:
        i += 1
        print(f'i = {i:3}')
        time.sleep(0.1) # 1초를 기다림.

        if stop_event.is_set():  # stop_event( )가 켜졌는지 확인을 합니다.
            return # break

def do_new(): # 숫자를 출력하고 1초를 기다린 뒤에 return:
    i = 0
    while True:
        i += 1
        print(f'i2= {i:3}')
        time.sleep(0.1) # 1초를 기다림.

        if stop_event2.is_set():  # stop_event( )가 켜졌는지 확인을 합니다.
            return # break


if __name__ == '__main__':     # We create another Thread
    action_thread = Thread(target=do_actions)
    action_new    = Thread(target=do_new    )
    action_new.start()  # do_action thread를 시작함.
    action_thread.start()  # do_action thread를 시작함.

    action_thread.join(timeout= 5) # 5초를 기다림.
    stop_event2.set() # stop 신호를 보냄
    action_new.join(timeout= 2) # 5초를 기다림.
    stop_event.set() # stop 신호를 보냄


    print(" 3초가 모두 지났습니다. 프로그램을 종료합니다. !")

