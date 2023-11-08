#!/usr/bin/python

# 초기화
from tkinter import *
window = Tk()

# 모델
counter = IntVar()
counter.set(0)

# 두 컨트롤러
def click_up():
    counter.set(counter.get() + 1)

def click_down():
    counter.set(counter.get() - 1)

# 뷰
frame = Frame(window)
frame.pack()

button = Button(frame, text="Up", command=click_up, bd=7, bg="yellow")
button.pack()

button = Button(frame, text="Down", bd=7, command=click_down, bg="lightgreen")
button.pack()

label = Label(frame, textvariable=counter) # 레이블을 변수롤 쓰는 방법
label.pack()

window.mainloop()
