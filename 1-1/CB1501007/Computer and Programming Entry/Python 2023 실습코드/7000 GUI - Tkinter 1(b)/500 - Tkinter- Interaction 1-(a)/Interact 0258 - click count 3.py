
# 초기화
from tkinter import *
window = Tk()

# 모델
counter = IntVar()
counter.set(0)

# 일반화된 컨트롤러
def click(var, value):
    var.set(var.get() + value)

# 뷰
frame = Frame(window)
frame.pack()

button = Button(frame, text="Up", command=lambda: click(counter, 1))
button.pack()

button = Button(frame, text="Down", command=lambda: click(counter, -1))
button.pack()

label = Label(frame, textvariable=counter)
label.pack()

window.mainloop()
