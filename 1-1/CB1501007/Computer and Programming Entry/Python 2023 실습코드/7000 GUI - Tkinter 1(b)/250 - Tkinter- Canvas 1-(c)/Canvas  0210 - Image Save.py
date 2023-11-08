#-------------------------------------------------------------------------------
# Purpose:     2020 컴퓨터및 프로그래밍 입문
# Author:      Cho
# Created:     2020-04-16
#-------------------------------------------------------------------------------


from tkinter import *
root = Tk()
root.title("부산대학교 만세당")
root.geometry("500x400+100+100")

cv = Canvas(root)
cv.create_rectangle(50,70,150,250, width=3, fill="orange")

cv.pack()
cv.postscript(file="CHO-2.ps", colormode='color')

root.mainloop()