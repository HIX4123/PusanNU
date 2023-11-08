#-------------------------------------------------------------------------------
# Purpose:     2020 컴퓨터및 프로그래밍 입문
# Author:      Cho
# Created:     2020-06-02
#-------------------------------------------------------------------------------
from tkinter import *
import sys

class Application(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.grid()
        self.createWidgets()
    def createWidgets(self):
        self.quitButton = Button(text='Quit',command=self.destroy) # Use destroy instead of quit
        self.quitButton.grid()

app = Application()
app.title("Sample application")
app.mainloop()