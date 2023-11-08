#-------------------------------------------------------------------------------
# Author:      Zoh
# Created:     2020-04-15
#-------------------------------------------------------------------------------


from tkinter import *

window = Tk()
window.title(" Computer Science 갈매기당 ")
#window.geometry("500x400+100+100")
#window.resizable(False, False)

width  = 500
height = 400


w = Canvas( window, width=width, height=height)
w.pack()

w.create_oval(50,  50, 200, 200, width=2, outline="red")
w.create_oval(150,220, 320, 280, width=2, fill="blue")

mainloop()
