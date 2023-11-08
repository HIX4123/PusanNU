
import random
from tkinter import *

root = Tk()
root.title("Particle - Brown Motion")
canvas = Canvas(root, width = 500, height = 500, bg = "khaki")
canvas.grid(row = 10, column = 10)
mymove = [-2, -1, 0, +1, +2]

canvas.create_line(20, 250, 480, 250) # 축을 그림
canvas.create_line(250, 20, 250, 480)

cx = 250
cy = 250
steps = 10000

for x in range( steps ) :
    newx = cx + random.choice(mymove)
    newy = cy + random.choice(mymove)
    canvas.create_line(cx, cy, newx, newy, fill="dark blue")
    cx = newx
    cy = newy

root.mainloop()