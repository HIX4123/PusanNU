
# Purpose:


import tkinter
import time

curtime = ''
clock = tkinter.Label( font = ( "맑은 고딕",30), fg="blue" )
clock.pack()

def tick():
    global curtime
    newtime = time.strftime('%H:%M:%S')
    if newtime != curtime:
        curtime = newtime
        clock.config(text=curtime)
    clock.after(500, tick)

tick()
clock.mainloop()
