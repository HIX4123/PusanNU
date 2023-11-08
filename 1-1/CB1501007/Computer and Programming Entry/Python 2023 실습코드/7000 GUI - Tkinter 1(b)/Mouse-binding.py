#-------------------------------------------------------------------------------
# Purpose:     2020 컴퓨터및 프로그래밍 입문
# Author:      Cho
# Created:     2020-05-25
#-------------------------------------------------------------------------------

"""
•<Button-1> 마우스 왼쪽 버튼 클릭
•<Button-2> 마우스 중간 버튼 클릭
•<Button-3> 마우스 오른쪽 버튼 클릭
•<Double-Button-1> 왼쪽 버튼 더블클릭
•<Return> Enter 키 눌려짐
•<Key> 키가 눌려짐
"""

from tkinter import *
root = Tk()

def click(event):
    print(f"> 클릭위치(x,y) {event.x:3},{event.y:3}")

def PNU(event) :
    print("우리 교수님 짱짱맨")



frame = Frame(root, width=300, height=300)

 #왼쪽 마우스 버튼 바인딩
frame.bind("<Button-1>", click)
frame.bind("<Button-3>", PNU  )

frame.pack()
root.mainloop()
