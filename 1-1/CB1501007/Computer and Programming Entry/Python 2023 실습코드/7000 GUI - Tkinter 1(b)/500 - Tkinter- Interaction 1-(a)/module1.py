#-------------------------------------------------------------------------------
# Purpose:     2020 컴퓨터및 프로그래밍 입문
# Author:      Cho
# Created:     2020-06-02
#-------------------------------------------------------------------------------

#!/usr/bin/

from tkinter import *
from tkinter import messagebox
import time, winsound, msvcrt

running = True

Freq = 2500
Dur = 150

top = Tk()
top.title('MapAwareness')
top.geometry('200x100') # Size 200, 200

def start():
       sec = 0
       while running:
           if sec % 1 == 0:
               winsound.Beep(Freq, Dur)

           time.sleep(1)
           sec += 1

def stop():
       running = False

startButton = top.Button(top, height=2, width=20, text ="Start", command = start)
stopButton = top.Button(top, height=2, width=20, text ="Stop", command = stop)

startButton.pack()
stopButton.pack()

top.mainloop()