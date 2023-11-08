#-------------------------------------------------------------------------------
# Purpose:     2020 컴퓨터및 프로그래밍 입문
# Author:      Cho
# Created:     2020-04-16
#-------------------------------------------------------------------------------


from tkinter import *
from PIL import ImageGrab
root = Tk()
cv = Canvas(root)
Myfont =  ( "맑은 고딕", 20)

root.title("부산대학교 만세당")
root.geometry("500x400+100+100")

cv.pack()

cv.create_rectangle(100,100,250,250, width=3)
cv.create_line([70, 130, 210, 80], fill='green', width=3)
cv.create_text( 290, 100, text="Good Girl", font=Myfont, fill='red')
cv.create_text( 290, 200, text="Good Boy", font=Myfont, fill='red')
cv.update()


#print(root.winfo_width())

def getter(widget):
    x=root.winfo_rootx()+widget.winfo_x()
    print(x)
    y=root.winfo_rooty()+widget.winfo_y()
    print(y)
    x1=x+widget.winfo_width()
    print(x1)
    y1=y+widget.winfo_height()
    print(y1)
    ImageGrab.grab().crop((x,y,x1,y1)).save("xem.jpg")

getter(cv)
root.mainloop()