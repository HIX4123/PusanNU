
from tkinter import *
import math
root = Tk()

canvas = Canvas(root)
canvas.pack(side='left')

#호(arc) 그리기
xy=10,10,150,150  #arc가 들어갈 외접 사각형
canvas.create_arc(xy, start=0, extent=270, fill="red")
canvas.create_arc(xy, start=270, extent=60, fill="blue")
canvas.create_arc(xy, start=330, extent=30, fill="green")

#사각형 그리기
canvas.create_rectangle(200, 200, 230, 230, fill='yellow', outline='blue')
canvas.create_rectangle(200, 200, 220, 220, fill='green', outline='white')


#polygon(다각형 그리기)
canvas.create_polygon(220, 10, 250, 10, 250, 30, 210, 50, 220, 80)

#파이(pi) 출력
print (math.pi)   #3.141592.....)


#[응용] 수학공식을 이용한 원 그리기
r=50
thick = 2
startx = 250  #중심점의 x축 평행이동
starty = 120  #중심점의 y축 평행이동
for i in range(360):
    x = r*math.cos((i*math.pi)/180)+startx   #호도법 사용
    y = r*math.sin((i*math.pi)/180)+starty
    canvas.create_oval(x, y, x+thick, y+thick)  #point 대신 oval(원)을 점으로 사용




root.title( u"다양한 기하 물체들")
root.mainloop()
