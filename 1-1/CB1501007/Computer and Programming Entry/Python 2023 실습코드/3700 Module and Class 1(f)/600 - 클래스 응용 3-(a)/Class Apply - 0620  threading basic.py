

import time
from threading import *

class MyThread(Thread): #
    def __init__(self):
        Thread.__init__(self) #

    def run(self):              #
        for el in range(10):    #
            print(self.getName(), el)
            time.sleep(0.01)

thread1 = MyThread()
thread2 = MyThread()
thread1.start()
thread2.start()
