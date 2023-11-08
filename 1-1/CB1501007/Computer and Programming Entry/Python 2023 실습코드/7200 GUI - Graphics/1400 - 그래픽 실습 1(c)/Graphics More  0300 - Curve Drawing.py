

from tkinter import *
root = Tk()

root.title(" 자유곡선 만들기")
cw = 500                                        # canvas width.
ch = 500                                        # canvas height.
canvas_1 = Canvas(root, width=cw, height=ch, background="white")
canvas_1.pack()               # show canvas on a grid item


Q=[ 30, 30, 50, 100, 20, 370, 200, 320, 340, 80, 100, 60, 320, 350]


canvas_1.create_line(Q, smooth='true', dash=(4), width=3)
canvas_1.create_line(Q, fill='red',  width=2)

root.mainloop()
