#-------------------------------------------------------------------------------
# Author:      Zoh
# Created:     2020-04-15
#-------------------------------------------------------------------------------

from tkinter import *
from PIL import ImageGrab

def checkered(canvas, line_distance):
   for x in range(line_distance,canvas_width,line_distance):
      canvas.create_line(x, 0, x, canvas_height, fill="#476042")

   for y in range(line_distance,canvas_height,line_distance):
      canvas.create_line(0, y, canvas_width, y, fill="#476042")


def save_canvas( root, canvas ):
    x = root.winfo_rootx() + canvas.winfo_x()
    y = root.winfo_rooty() + canvas.winfo_y()
    xx = x + w.winfo_width()
    yy = y + w.winfo_height()
    ImageGrab.grab(bbox=(x, y, xx, yy)).save("test2.gif")




master = Tk()
canvas_width = 500
canvas_height = 400
w = Canvas(master, width=canvas_width, height=canvas_height)
w.pack()

gap = 25
checkered(w, gap )
w.update()

save_canvas( master, w )

#master.after(1000, save_canvas)

mainloop()

