
from tkinter import Tk, Frame, Button, BOTH, SUNKEN, RIDGE
import tkinter.colorchooser

class Example(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.initUI()

    def initUI(self):
        self.parent.title("Color chooser")
        self.pack(fill=BOTH, expand=1)

        self.btn = Button(self, text= "색을 선택하세요",\
            relief= RIDGE, bg="green", command=self.onChoose)
        self.btn.place(x=30, y=30)

        self.frame = Frame(self, border=5,
            relief=SUNKEN, width=100, height=100)
        self.frame.place(x=160, y=30)

    def onChoose(self):
        (rgb, hx) = tkinter.colorchooser.askcolor()
        print("당신이 선택한 색상 (rgb, hx) =", (rgb, hx))
        self.frame.config(bg=hx)


root = Tk()
ex = Example(root)
root.geometry("300x150+300+300")
root.mainloop()

