#Tkinter -- Canvas의 사용법을 배웁니다. (Text)


from tkinter import *
import math

root = Tk()
root.title( "텍스트 활용해보기")
canvas = Canvas(root)
canvas.grid(row=200, column=200)


#[응용] 수학공식을 이용한 텍스트 배치
myText=['P', 'r', 'o', 'b', 'l', 'e', 'm', ' ', 'S', 'o', 'l', 'v', 'i', 'n', 'g']

r=80
thick = 2
startx = 200  #중심점의 x축 평행이동
starty = 120  #중심점의 y축 평행이동

for i in range(len(myText)):
    angle=i*20+180
    x = r*math.cos((angle*math.pi)/180)+startx   #호도법 사용
    y = r*math.sin((angle*math.pi)/180)+starty
    canvas.create_text(x, y, text=myText[i], font='Arial 20')


root.mainloop()
