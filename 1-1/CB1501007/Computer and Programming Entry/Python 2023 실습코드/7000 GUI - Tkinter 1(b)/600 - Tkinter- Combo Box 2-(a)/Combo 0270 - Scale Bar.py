
from tkinter.ttk import Frame, Label, Scale, Style
from tkinter import Tk, BOTH, IntVar


class Example(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.initUI()

    def initUI(self):
        self.parent.title("Scale")
        self.style = Style()
        self.style.theme_use("default")

        self.pack(fill=BOTH, expand=1)

        scale = Scale(self, from_=0, to=100, command=self.onScale)
        scale.place(x=20, y=20)

        self.var = IntVar()
        self.label = Label(self, text=0, textvariable=self.var)
        self.label.place(x=130, y=70)

    def onScale(self, val):
        v = int(float(val))
        print("당신이 선택한 값은 Scale value=", v)
        self.var.set(v)



root = Tk()
ex = Example(root)
root.geometry("300x150+300+300")
root.mainloop()

