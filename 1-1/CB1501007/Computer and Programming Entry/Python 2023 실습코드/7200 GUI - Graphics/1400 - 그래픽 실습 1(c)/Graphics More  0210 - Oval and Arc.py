
from tkinter import *
root = Tk()
root.title('원관련 canvas object')

cw = 600                                      # canvas width
ch = 600                                      # canvas height
canvas_1 = Canvas(root, width=cw, height=ch, background="grey")
canvas_1.grid(row=0, column=1)
canvas_1.pack()

xy_1 = 100,   100,  300,  300
xy_2 = 20,  130,  80, 100
xy_3 = 100, 130, 140,  20
xy_4 = 300, 300, 550, 450

canvas_1.create_arc(xy_1, start= 20, extent= 270, fill="red", outline="white", width=3)
canvas_1.create_oval(xy_4, outline="black", fill="orange", width=5)

root.mainloop()
