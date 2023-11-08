#-------------------------------------------------------------------------------
# Author:      Zoh
# Created:     2020-04-15
#-------------------------------------------------------------------------------

from tkinter import *

canvas_width = 500
canvas_height =400
python_green = "#476042"

master = Tk()

w = Canvas(master,
           width=canvas_width,
           height=canvas_height)
w.pack()

points = [   0,0, \
            canvas_width,canvas_height/2, \
            0, canvas_height,   \
            canvas_width/2 ,canvas_height ]

w.create_polygon(points, outline=python_green,
            fill='yellow', width=3, alpha=0.5)

mainloop()
