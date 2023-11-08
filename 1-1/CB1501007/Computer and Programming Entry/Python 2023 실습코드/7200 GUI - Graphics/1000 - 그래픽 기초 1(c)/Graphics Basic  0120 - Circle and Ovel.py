

from tkinter import *

canvas_width = 600
canvas_height =400

master = Tk()

w = Canvas(master, width=canvas_width, height=canvas_height)
w.pack()

w.create_oval(50,50,300,300, width=4, fill="green")

mainloop()
