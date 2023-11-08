
#Tkinter -- Canvas의 사용법을 배웁니다. (Line2)


from tkinter import *
root = Tk()

#Canvas 생성
cw = 400                                      # canvas width
ch = 300                                      # canvas height
canvas = Canvas(root, width=cw, height=ch, background="Lightgreen")
canvas.grid(row=0, column=1)

#Dashed Arrow Line 그리기
x_start = 20
y_start = 20
x_end = 180
y_end = 20
canvas.create_line(x_start, y_start, x_end, y_end, dash=(3), arrow = "first", width = 3)

#굵은 점선(Dashed) 그리기 1
x_start= x_end
y_start= y_end
x_end= 50
y_end= 70
canvas.create_line(x_start, y_start, x_end, y_end, dash=(9), width = 5, fill= "red")

#굵은 점선(Dashed) 그리기 2
x_start= x_end
y_start= y_end
x_end= 150
y_end= 70
canvas.create_line(x_start, y_start, x_end, y_end, dash=(19), width= 15, caps="round", fill= "dark blue")

#일반 직선 그리기
x_start= x_end
y_start= y_end
x_end= 80
y_end= 100
canvas.create_line(x_start, y_start, x_end, y_end, fill="purple")


root.title( "여러가지 라인 타입들")
root.mainloop()
