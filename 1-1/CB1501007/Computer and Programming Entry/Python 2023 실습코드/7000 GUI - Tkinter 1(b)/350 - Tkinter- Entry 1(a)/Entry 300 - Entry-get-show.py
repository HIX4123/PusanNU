
from tkinter import *

master = Tk()
etext = Entry(master)

etext.pack()
etext.focus_set()  # 커서를 이쪽으로 옮겨서 준비하도록 한다.

def callback():
    entertxt= etext.get()
    if entertxt=="":
        print("You did not gave any text")
    else :
        print("Typed Text=", etext.get())

mybutton = Button(master, text="GET", width=10, command=callback)
mybutton.pack()

mainloop()


