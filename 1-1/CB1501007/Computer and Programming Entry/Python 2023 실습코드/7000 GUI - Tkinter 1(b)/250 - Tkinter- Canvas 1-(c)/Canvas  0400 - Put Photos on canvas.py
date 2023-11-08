#-------------------------------------------------------------------------------
# Author:      Zoh
# Created:     2020-04-15
#-------------------------------------------------------------------------------

from tkinter import *

canvas_width  = 1000
canvas_height = 1000

master = Tk()
master.title("How to put an image:")

canvas = Canvas(master, width=canvas_width, height=canvas_height)


# PhotoImage class는  can only read GIF and PGM/PPM images from files
my_img = PhotoImage( file="coffee-cup.gif")
canvas.create_image( 620, 750, anchor=NW, image= my_img)
your_img = PhotoImage( file="dish.gif")
canvas.create_image(  50, 50, anchor=NW, image= your_img)
canvas.pack()

mainloop()
