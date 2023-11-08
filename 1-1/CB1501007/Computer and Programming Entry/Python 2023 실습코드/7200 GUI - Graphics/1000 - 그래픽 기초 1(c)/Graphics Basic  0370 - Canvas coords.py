
from tkinter import *

master = Tk()

W=600
H=500
w = Canvas(master, width=W, height=H)
w.pack()

w.create_line(0, 0, W, H)
w.create_line(0, H, W, 0, fill="red", dash=(4, 4), width=4)

w.create_rectangle(50, 25, 150, 75, fill="blue")

# Note that items added to the canvas are kept until you remove them.
# If you want to change the drawing, you can either use methods like coords,
# itemconfig, and move to modify the items, or use delete to remove them.

xy = ( 10, 10, 200, 300 )
i = w.create_line(xy, fill="red")

new_xy = ( 200, 200, 100, 400)
w.coords(i, new_xy) # change coordinates
w.itemconfig(i, fill="blue") # change color

w.delete(i) # remove

#w.delete(ALL) # remove all items

mainloop()
