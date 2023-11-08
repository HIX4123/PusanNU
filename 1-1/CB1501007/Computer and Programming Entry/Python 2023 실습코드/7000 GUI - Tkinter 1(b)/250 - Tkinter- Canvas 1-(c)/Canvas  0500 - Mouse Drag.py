#-------------------------------------------------------------------------------
# Author:      Zoh
# Created:     2020-04-15
#-------------------------------------------------------------------------------

from tkinter import *

canvas_width = 500
canvas_height = 500

def paint( event ):
   python_green = "#476542"
   x1, y1 = ( event.x - 1 ), ( event.y - 1 )
   x2, y2 = ( event.x + 1 ), ( event.y + 1 )
   #w.create_oval( x1, y1, x2, y2, fill = python_green )
   w.create_rectangle( x1, y1, x1-1, y1+1, fill = python_green )

master = Tk()
master.title( "Painting using Ovals" )
w = Canvas(master, width=canvas_width, height=canvas_height)
w.pack(expand = YES, fill = BOTH)
w.bind( "<B1-Motion>", paint )

message = Label( master, text = "Press and Drag the mouse to draw" )
message.pack( side = BOTTOM )

mainloop()
