
# 상대좌표가 아닌 절대 좌표 row와 column으로 배치 함

from tkinter import *

colours = ['red','green','orange','white','yellow','blue']

r = 0
for c in colours:
    Button(text=c, relief=RAISED, width=10).grid(row=r,column=0 )
    Entry(bg=c,    relief=SUNKEN, width=10).grid(row=r,column=1)
    r = r + 1

mainloop()
