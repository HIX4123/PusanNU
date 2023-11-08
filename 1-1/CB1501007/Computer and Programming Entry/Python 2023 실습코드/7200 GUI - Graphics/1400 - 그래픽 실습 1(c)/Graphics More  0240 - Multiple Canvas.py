
#Tkinter -- Canvas의 사용법을 배웁니다. (Line)


from tkinter import *
import math
root = Tk()

canvas = Canvas(root, width=500, height=300, bg="orange")
canvas.pack(side=RIGHT )


canvas.create_line(0, 0, 50, 50) #기본 직선
canvas.create_line(50, 50, 100, 100, width=10, fill="red") #굵은 빨간 직선
canvas.create_line(30, 10, 80,   50, width=10, fill="blue", arrow=BOTH) #굵은 파란 양쪽 화살표 직선
canvas.create_line(50, 10, 100,  10, width=10, arrow='last') #굵은 검은 한쪽 화살표 직선
canvas.create_line(110, 10, 110, 20, 120, 20, 120, 30, 130, 30, 130, 40) #계단 모양

xy=(80, 50, 10, 100, 100, 130, 20, 50) #Bezier 곡선
canvas.create_line(xy, width=3, smooth=1)

canvas2 = Canvas(root, bg="khaki")
canvas2.pack(  )
canvas2.create_line(0, 0, 500, 500, width=4) #기본 직선
canvas2.create_line(0, 200, 400, 10, width=4)

root.title(" 하나 이상의 캔버스 공간 사용하기")
root.mainloop()
