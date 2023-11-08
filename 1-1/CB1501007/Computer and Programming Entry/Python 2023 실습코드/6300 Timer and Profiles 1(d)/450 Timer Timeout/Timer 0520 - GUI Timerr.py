#-------------------------------------------------------------------------------
# Purpose:     2020 컴퓨터및 프로그래밍 입문
# Author:      Cho
# Created:     2020-06-02
#-------------------------------------------------------------------------------
from threading import Timer, Thread, Event
from datetime import datetime
import tkinter as tk

app = tk.Tk()
lab = tk.Label(app, text="Timer will start in a sec", height=2, width=20)
lab.pack()


class perpetualTimer():

    def __init__(self, t, hFunction):
        self.t = t
        self.hFunction = hFunction
        self.thread = Timer(self.t, self.handle_function)

    def handle_function(self):
        self.hFunction()
        self.thread = Timer(self.t, self.handle_function)
        self.thread.start()

    def start(self):
        self.thread.start()

    def cancel(self):
        self.thread.cancel()


def printer():
    tempo = datetime.today()
    clock = "{}:{}:{}".format(tempo.hour, tempo.minute, tempo.second)
    try:
        lab['text'] = clock
    except RuntimeError:
        exit()


t = perpetualTimer(1, printer)
t.start()
app.mainloop()
