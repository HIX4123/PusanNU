
from tkinter import *


#현재 마우스 포인터와 가장 가까운 아이템을 찾는 함수
def curpos(event) :
    global x, y, item
    x = event.x
    y = event.y
    item = canvas.find_closest(x,y)  #클릭한 마우스의 좌표와 가장 가까운 아이템 찾기


def moveitem(event) : #선택된 아이템을 이동시키는 함수
    global x, y
    nx = event.x
    ny = event.y
    distx = nx - x
    disty = ny - y
    canvas.move(item, distx, disty)
    x = nx
    y = ny


root = Tk()
canvas = Canvas(root)
canvas.pack(side='left', fill=BOTH)

#기본 도형 추가
line = canvas.create_line(0, 0, 500, 500, width=5, fill="green")
circle = canvas.create_oval(50, 50, 150, 150, width=5, fill="blue")
rect = canvas.create_rectangle(70, 70, 180, 180, width=5, fill="yellow")


#이미지 아이콘 추가
photo = PhotoImage(file='android.gif')
icon = canvas.create_image(250, 100, image=photo)


canvas.bind("<Button-1>", curpos)  #한번 클릭
canvas.bind("<B1-Motion>", moveitem) #클릭한 다음 이동(드래그)


root.title( u"마우스로 물건 찝어 옮기기")
root.mainloop()

