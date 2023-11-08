# textvariable을 이용해서 숫자를 바로 문자로 바꾼다.

from tkinter import *

def click():
    counter.set(counter.get() + 1)


window = Tk()

counter = IntVar()  # event 변수임을 선언한다.
counter.set(0)      # 초기값은 0으로 만든다.


frame = Frame(window)
frame.pack( )

button = Button(frame, text="Click", bg="orange", command=click, bd=3)
button.pack( )

label = Label(frame, textvariable=counter) # 텍스트를 변수로 만든다. 변수 !!!!
label.pack( )

window.mainloop()
