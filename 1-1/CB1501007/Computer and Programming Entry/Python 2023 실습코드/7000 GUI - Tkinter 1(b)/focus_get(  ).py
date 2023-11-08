#-------------------------------------------------------------------------------
# Purpose:     2020 컴퓨터및 프로그래밍 입문
# Author:      Cho
# Created:     2020-05-25
#-------------------------------------------------------------------------------


from tkinter import *
from tkinter.ttk import *

master = Tk()

def focus(event):
    widget = master.focus_get() # focus된 widget을 가지고 온다.
    print( f' Widget={widget} has a focus')


e1 = Entry(master)
e1.pack(expand = 1, fill = BOTH)


e2 = Button(master, text ="Button")
e2.focus_set()
e2.pack(pady = 5)


e3 = Radiobutton(master, text ="Hello")
e3.pack(pady = 5)

# Here function focus() is binded with Mouse Button-1
# so every time you click mouse, it will call the
# focus method, defined above
master.bind_all("<Button-1>", lambda e: focus(e))

mainloop()

