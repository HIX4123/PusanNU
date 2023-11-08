
from tkinter import *

canvas_width = 400
canvas_height =400
master = Tk()
master.title( "다각형 만들기(Polygon)")

w = Canvas(master, width=canvas_width, height=canvas_height)
w.pack()


N=300
w.create_line( 0,0 ,   N, N, width=4)
w.create_line( 155,55 ,   56,256, width=3, fill='red')  # 점찍기
w.create_text(150,100, font=("맑은 고딕",20), fill="blue", text="이것은 한글이다")

gap=  80
sx = 100
sy = 100
points = [ sx, sy,  sx+gap, sy,  sx+gap, sy+gap, sx, sy+gap ]
w.create_polygon(points, outline="red", fill='yellow', width=3)


mainloop()