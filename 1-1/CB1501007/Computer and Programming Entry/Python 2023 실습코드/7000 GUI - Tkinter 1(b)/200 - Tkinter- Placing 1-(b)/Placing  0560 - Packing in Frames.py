
# 3개의 frame을 사용해서 GUI를 구성한다.
#

from tkinter import *

window = Tk()
frame = Frame(window)
frame.pack()

first = Label(frame, text="First label")
first.pack()

frame2 = Frame(window, borderwidth=4, relief= RAISED)
frame2.pack()

myf_01  = Label(frame2, text="Inner 01 label")
myf_01.pack(side= BOTTOM)
myf_02  = Label(frame2, text="Inner 02 label")
myf_02.pack(side= BOTTOM)

frame3 = Frame(window, borderwidth=4, relief= RAISED)
frame3.pack()

myf_03  = Label(frame3, text="Inner 03 label", padx=10, pady=10)
myf_03.pack(side=RIGHT)
myf_04  = Label(frame3, text="Inner 04 label")
myf_04.pack(side=TOP)
myf_05  = Label(frame3, text="Inner 05 label", bg="red")
myf_05.pack(side=TOP)
myf_06  = Label(frame3, text="Inner 06 label", fg="red")
myf_06.pack(side=RIGHT)
myf_07  = Label(frame3, text="Inner 07 label", bg="orange")
myf_07.pack(side=RIGHT)
myf_08  = Label(frame3, text="Inner 08 label", bg="green")
myf_08.pack(side=RIGHT)
myf_09  = Label(frame3, text="Inner 09 label", bg="blue", fg='white')
myf_09.pack(side=TOP)

window.mainloop()
