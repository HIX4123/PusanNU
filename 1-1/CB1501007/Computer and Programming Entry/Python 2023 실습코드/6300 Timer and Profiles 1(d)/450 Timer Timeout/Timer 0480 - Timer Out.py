#-------------------------------------------------------------------------------
# Purpose:     2020 컴퓨터및 프로그래밍 입문
# Author:      Cho
# Created:     2020-06-02
#-------------------------------------------------------------------------------
from threading import Timer
import sys

def scheduled_task(arg):
       print("\ntask complete arg %s!\n"%(arg))

def run_scheduled_task(arg):
       timer = Timer(10, scheduled_task, [arg])
       timer.start()

done = False
while not done:
       user_input = input("Give me some input (exit to stop): ")
       if user_input == 'exit':
           print('Exiting')
           done = True
       else:
           run_scheduled_task(user_input)