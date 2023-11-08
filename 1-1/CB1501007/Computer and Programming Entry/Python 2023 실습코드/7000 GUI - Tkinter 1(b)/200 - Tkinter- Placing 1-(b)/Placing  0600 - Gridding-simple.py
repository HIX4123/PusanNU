
# 줄 맞추어서 놓기
from tkinter import *

root = Tk()
root.title("자유롭게 사용하기 연습")

w = Label(root, text="Additive:")
w.grid(row=1500, column=1200)
w = Label(root, text="Subtractive:")
w.grid(row=1700, column=1100)

w = Label(root, text="Cyan", bg="cyan", height=2)
w.grid(row=1000, column=1100)
w = Label(root, text="Magenta", bg="magenta", fg="white")
w.grid(row=1000, column=1200)
w = Label(root, text="Yellow", bg="yellow", height=2)
w.grid(row=1000, column=1300)

w = Label(root, text="Red", bg="red", fg="white", height=2)
w.grid(row=300, column=1100)
w = Label(root, text="Green", bg="green", height=2)
w.grid(row=300, column=1200)
w = Label(root, text="Blue", bg="blue", fg="white")
w.grid(row=300, column=1300)

mainloop()