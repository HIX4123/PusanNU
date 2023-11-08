
from tkinter import *
import random

master = Tk()

cx = 600
cy = 600
gap = 10
w = Canvas(master, width=cx, height=cy )
Myfont =  ( "맑은 고딕", 20)


for my in range(50):
    x = random.randrange( gap,cx-gap )
    y = random.randrange( gap,cy-gap )
    w.create_text( x, y, font = Myfont, fill="blue", text='*')


for my in range(110):
    ux = random.randrange( gap,cx-gap )
    uy = random.randrange( gap,cy-gap )
    vx = random.randrange( gap,cx-gap )
    vy = random.randrange( gap,cy-gap )
    w.create_line( ux, uy, vx, vy, fill="orange",  width=2)

w.pack()

mainloop()
