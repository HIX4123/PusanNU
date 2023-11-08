# 임의의 함수 f(x)를 그려봅시데이...

from tkinter import *
import math

root = Tk()

width = 360
height = 300

vcenter = height/2
hcenter = width/2

y_amplitude = 100 #sin, cos함수의 최대값은 1이기 때문에 그림으로 나타내기 위해 증폭


#Canvas 생성
canvas = Canvas(root, width=width, height=height, bg='white')
canvas.pack(side='left')

# sin()
for x in range(720):
    y = math.sin((x*math.pi)/180)*y_amplitude + vcenter
    sinLine = canvas.create_line(x, y, x+1, y+1, fill='red')

# cos()
for x in range(720):
    y = math.cos((x*math.pi)/180)*y_amplitude + vcenter
    sinLine = canvas.create_line(x, y, x+1, y+1, fill='blue')

#좌표축 생성
canvas.create_line(hcenter, 0, hcenter, height)
canvas.create_line(0, vcenter, width, vcenter)

#Text 출력
canvas.create_text( 30, 10, text="sin = red", fill='red')
canvas.create_text(100, 10, text="cos = blue", fill='blue')

root.title( u" 함수 커브 그리기 ")
root.mainloop()