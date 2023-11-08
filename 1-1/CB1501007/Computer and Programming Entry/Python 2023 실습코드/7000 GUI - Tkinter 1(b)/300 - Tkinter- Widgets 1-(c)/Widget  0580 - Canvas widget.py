
from tkinter import *
master = Tk()
master.title("이거 머꼬?")

canvas_width = 800
canvas_height = 600
w = Canvas(master, width=canvas_width, height=canvas_height)
w.pack()


w.create_rectangle(550, 200, 550, 400, fill="#476042")    # outer box
w.create_rectangle(365, 135, 535, 365, fill="yellow")     # inner box
w.create_line(  0,   0,  550,  200, fill="#476042", width=3)
w.create_line(  0, 100,  550,  800, fill="#476042", width=3)
w.create_line(550,  20, 200,   0, fill="#476042", width=3)
w.create_line(150,  80, 800, 100, fill="#476042", width=3)


mainloop()
