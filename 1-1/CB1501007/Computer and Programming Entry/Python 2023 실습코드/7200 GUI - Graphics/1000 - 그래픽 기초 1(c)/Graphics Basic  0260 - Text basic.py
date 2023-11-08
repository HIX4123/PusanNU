#Tkinter -- Canvas의 사용법을 배웁니다. (Text)


from tkinter import *
import math

root = Tk()
root.title( "텍스트 활용해보기")
canvas = Canvas(root)
canvas.grid(row=100, column=100)


###사각형 좌표 출력
##coord = 120, 130, 280, 200
##canvas.create_rectangle(coord, fill='yellow', outline='blue')
##canvas.create_text(coord[0], coord[1], text='('+str(coord[0])+','+str(coord[1])+')')
##canvas.create_text(coord[0], coord[3], text='('+str(coord[0])+','+str(coord[3])+')')
##canvas.create_text(coord[2], coord[1], text='('+str(coord[2])+','+str(coord[1])+')')
##canvas.create_text(coord[2], coord[3], text='('+str(coord[2])+','+str(coord[3])+')')

#Text 그리기? 나타내기?
x=50
y=30
canvas.create_text(x, y, text="Hello?", fill='red')
xy=90, 60
canvas.create_text(xy, text="Welcome!", font='Arial 20', fill='blue')
xy=120, 90
canvas.create_text(xy, text="Tkinter~", font='Courier 15 bold', fill='Green')
xy=150, 110
canvas.create_text(xy, text="컴퓨터공학과", font=('맑은 고딕', 35) , fill='purple')
xy=180, 240
canvas.create_text(xy, text="파이썬 입문", font=('나눔명조', 30) , fill='black')




root.mainloop()
