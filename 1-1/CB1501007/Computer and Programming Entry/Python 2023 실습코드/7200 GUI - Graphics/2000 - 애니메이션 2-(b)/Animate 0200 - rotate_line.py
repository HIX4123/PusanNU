
#Tkinter -- Canvas의 사용법을 배웁니다. (움직이는 선에 대한 simulation)

from tkinter import *
import time
import math
root = Tk()
root.title(" 시계 만들어 보기 ")

cw = 220                                      # canvas width
ch = 180                                      # canvas height
chart_1 = Canvas(root, width=cw, height=ch, background="lightgreen")
chart_1.grid(row=0, column=0)

cycle_period = 50   # pause duration (milliseconds).

p1_x = 90.0
p1_y = 90.0

p2_x = 180.0
p2_y = 160.0

a_radian = math.atan((p2_y - p1_y)/(p2_x - p1_x))
a_length = math.sqrt((p2_y - p1_y)*(p2_y - p1_y) +\
                     (p2_x - p1_x)*(p2_x - p1_x))

for i in range(1,300):       # 300 position 이동 후 프로그램 종료

    a_radian +=0.05
    p1_x = p2_x - a_length * math.cos(a_radian)
    p1_y = p2_y - a_length * math.sin(a_radian)

    chart_1.create_line(p1_x, p1_y, p2_x, p2_y)
    chart_1.update()
    chart_1.after(cycle_period)
    chart_1.delete(ALL)
    if ( i % 30 == 0 ) : print("Keep Going", i/ 300.0)

root.mainloop()

