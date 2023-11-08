#-------------------------------------------------------------------------------
# Purpose:     2019 Power Python
# Author:      Cho
#-------------------------------------------------------------------------------

from tkinter import *
import tkinter.font

window=tkinter.Tk()
window.title("컴퓨터 시스템 입문 연습하기 ")
window.geometry("640x400+100+100")
window.resizable(True, True)
window.configure(background='plum')

myfont    = tkinter.font.Font(family="나눔명조",  size=44, slant="italic")
bold_font = tkinter.font.Font(family="Helvetica", size=62, weight="bold")


label=Label(window, text="  파이썬 3.7.2  ", font=myfont, \
                    foreground="tomato")
label.pack(side=TOP) # TOP, LEFT, RIGHT, BOTTOM

label=Label(window, text="  컴퓨터공학부  ", font=bold_font, \
                    background="black", foreground="tomato")
label.pack(side=BOTTOM)

label=Label(window, text="  오늘 종강이다.ㅋㅋㅋ", font=myfont, \
                    background="black", foreground="tomato")
label.pack(side=BOTTOM)


window.mainloop()