
from tkinter import *

master = Tk()

W=600
H=500
w = Canvas(master, width=W, height=H)
w.pack()

w.create_line(0, 0, W, H, width=4 )
w.create_line(0, H, W, 0, fill="red", dash=(4, 4), width=4)

w.create_rectangle( W/2, H/2, W/2+200, H/2+200, fill="blue")

# Note that items added to the canvas are kept until you remove them.
# If you want to change the drawing, you can either use methods like coords,
# itemconfig, and move to modify the items, or use delete to remove them.

xy = ( 300, 10, 200, 300 )
myline = w.create_line(xy, width=5, fill="red")

new_xy = ( 200, 200, 100, 400)
w.coords( myline, new_xy) # change coordinates
w.itemconfig( myline, fill="orange") # change color


for i in range(10):
    w.coords( myline, 110, 310, 100+i*20, 200+i+30) # change coordinates
    w.after(500)
#    w.itemconfig( myline, fill="blue") # change color
    w.update()

#w.delete( myline) # remove
#w.delete(ALL) # remove all items

mainloop()
