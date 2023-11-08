
# 상대좌표가 아닌 절대 좌표 row와 column으로 배치 함

from tkinter import *

root = Tk(  )
root.title("Grid Spacing Layout")
for r in range(6):
    for c in range(8):
        myl = Label(root, text='R%s/C%s'%(r,c),  font=("Arial", 25), borderwidth=1 )
        myl.grid(row=r,column=c)


root.mainloop(  )