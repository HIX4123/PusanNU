#-------------------------------------------------------------------------------
# Purpose:     2020 컴퓨터및 프로그래밍 입문
# Author:      Cho
# Created:     2020-05-25
#-------------------------------------------------------------------------------


from tkinter import *
from tkinter.ttk import *


master = Tk()


e1 = Entry(master)
e1.pack(expand = 1, fill = BOTH)

# Button widget which currently has the focus
e2 = Button(master, text ="Button")

# here focus_set() method is used to set the focus
# Sets focus to w, so that all keyboard events for the application are sent to w.
e2.focus_set()  # 탭 키를 이용해서 옮길 수 있다. 그리고 spacE로 입력함.
e2.pack(pady = 5)

# Radiobuton widget
e3 = Radiobutton(master, text ="Hello")
e3.pack(pady = 5)

# Infinite loop
mainloop()

