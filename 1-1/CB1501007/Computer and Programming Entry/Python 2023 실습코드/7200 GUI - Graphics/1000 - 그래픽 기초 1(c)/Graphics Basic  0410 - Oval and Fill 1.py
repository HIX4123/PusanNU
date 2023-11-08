

from tkinter import *

W = 1000
H = 600

master = Tk()

mypaper = Canvas(master, width= W, height=H )
mypaper.pack()

xgap = 100
csize = 50
leftx = 150
lefty = 150
for w in range(7):
    mypaper.create_oval( leftx, lefty, leftx+csize, lefty+csize, width=2, fill="orange")
    leftx += xgap


mainloop()
