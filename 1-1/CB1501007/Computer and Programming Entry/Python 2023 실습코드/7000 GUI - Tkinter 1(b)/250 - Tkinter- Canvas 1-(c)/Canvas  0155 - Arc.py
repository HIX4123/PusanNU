#-------------------------------------------------------------------------------
# Author:      Zoh
# Created:     2020-04-15
#-------------------------------------------------------------------------------

from tkinter import *

top = Tk()

C = Canvas(top, bg="khaki", height=250, width=300)

coord = 10, 50, 240, 210
arc = C.create_arc(coord, start=0, extent=120, fill="red")

C.pack()
top.mainloop()