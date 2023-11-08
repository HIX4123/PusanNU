
# 상대좌표가 아닌 절대 좌표 row와 column으로 배치 함

from tkinter import *

root = Tk(  )
root.title("Grid Spacing Layout")

for r in range(6):
    for c in range(8):
        mytext=' [R%s/C%s] '%(r,c)
        if (r+c) %2 == 0  :
            mycolor="orange"
        else :
            mycolor="ivory"

        myl = Button(root, text=mytext, font=(14), borderwidth=2, bg=mycolor, relief=RAISED )
        myl.grid(row=r,column=c)


root.mainloop(  )