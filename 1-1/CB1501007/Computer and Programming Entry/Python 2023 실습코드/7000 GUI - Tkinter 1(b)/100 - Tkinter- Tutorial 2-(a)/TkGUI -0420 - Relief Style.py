# !/usr/bin/python3
from tkinter import *
import tkinter

import tkinter.font

top = Tk()


myfont= tkinter.font.Font(family="나눔명조", size=24, slant="italic")

B1 = Button(top, text = "돼지국밥",   relief = FLAT, font=myfont, width=15 )
B2 = Button(top, text = "소고기국밥", relief = RAISED, font=myfont,width=15 ,\
            fg="red", bg="yellow", bd=10 )
B3 = Button(top, text = "라면2", relief = RAISED, font=myfont, width=15)
B4 = Button(top, text = "쌀국수", relief = GROOVE,font=myfont,  bd=10, width=15 )
B5 = Button(top, text = "김김밥밥",  relief = RIDGE, font=myfont,width=15 )

B1.pack()
B2.pack()
B3.pack()
B4.pack()
B5.pack()
top.mainloop()