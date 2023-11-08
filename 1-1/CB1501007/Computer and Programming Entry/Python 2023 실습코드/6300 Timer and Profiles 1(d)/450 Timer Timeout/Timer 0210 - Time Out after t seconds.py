#-------------------------------------------------------------------------------
# Purpose:     2020 컴퓨터및 프로그래밍 입문
# Author:      Cho
# Created:     2020-06-02
#-------------------------------------------------------------------------------

from threading import Thread, Event
import time



stop_event = Event() # Event 객체를 사용. Thread로 넘겨 줌


def do_actions(): # 숫자를 출력하고 1초를 기다린 뒤에 return:
    i = 0
    while True:
        i += 1
        print(f'기다림. i={i}')
        mycode = input("뭐라도 치시오:")
        print(i, list(mycode))

        #time.sleep(1) # 1초를 기다림.

        if stop_event.is_set():  # stop_event( )가 켜졌는지 확인을 합니다.
            break


if __name__ == '__main__':     # We create another Thread
    action_thread = Thread(target=do_actions)
    action_thread.start()  # do_action thread를 시작함.
    action_thread.join(timeout=5) # 5초를 기다림.
    stop_event.set() # stop 신호를 보냄


    print(" 5초가 모두 지났습니다. 프로그램을 종료합니다. !")

