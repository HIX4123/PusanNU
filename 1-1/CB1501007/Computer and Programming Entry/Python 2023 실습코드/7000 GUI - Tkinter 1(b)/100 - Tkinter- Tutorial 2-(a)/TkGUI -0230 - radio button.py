# !/usr/bin/python3
from tkinter import *


root = Tk()
root.option_readfile('optionDB')
root.title('Radiobutton')

fruit=[('Passion fruit', 1), ('Loganberries', 2), ('Mangoes in syrup', 3),
       ('Oranges', 4), ('Apples', 5), ('Grapefruit', 6)]

var = IntVar()  # 정수값을 받도록 설정한다.
print("var=", var)

for text, value in fruit:
    Radiobutton(root, text=text, value=value, variable=var).pack(anchor=W)
    # W는 왼쪽


var.set(3)  # 초기화하는 방법
root.mainloop()

