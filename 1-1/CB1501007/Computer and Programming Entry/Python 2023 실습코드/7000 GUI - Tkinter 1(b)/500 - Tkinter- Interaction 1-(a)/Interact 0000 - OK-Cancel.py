
from tkinter import *
import tkinter.simpledialog

class MyDialog(tkinter.simpledialog.Dialog):

    def body(self, master):
        Label(master, text="First:").grid(row=0)
        Label(master, text="Second:").grid(row=1)

        self.e1 = Entry(master)
        self.e2 = Entry(master)

        self.e1.grid(row=0, column=1)
        self.e2.grid(row=1, column=1)
        return self.e1 # initial focus

    def apply(self):
        first  = (self.e1.get())
        second = (self.e2.get())
        self.result = first, second
        print("we get", first, second)

root = Tk()
d = MyDialog(root, 'test window')
root.destroy( )

