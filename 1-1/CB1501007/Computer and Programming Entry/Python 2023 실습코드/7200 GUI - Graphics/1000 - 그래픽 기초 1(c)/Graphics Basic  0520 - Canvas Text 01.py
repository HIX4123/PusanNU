
from tkinter import *

canvas_width = 500
canvas_height = 500

colours = ("#476042", "yellow")
box=[]

for ratio in ( 0.2, 0.35 ):
   box.append( (canvas_width * ratio,
                canvas_height * ratio,
                canvas_width * (1 - ratio),
                canvas_height * (1 - ratio) ) )

master = Tk()

w = Canvas(master, width=canvas_width, height=canvas_height)
w.pack()

for i in range(2):
   w.create_rectangle(box[i][0], box[i][1],box[i][2],box[i][3], fill=colours[i])

w.create_text(canvas_width / 2, canvas_height / 2, text="Python")
w.create_text(110, 210, text="이것은 사람이다.", font=("맑은 고딕", 23), fill="red")
w.create_text(310, 410, text="미친 것 아냐?", font=("맑은 고딕", 33), fill="red")
mainloop()
