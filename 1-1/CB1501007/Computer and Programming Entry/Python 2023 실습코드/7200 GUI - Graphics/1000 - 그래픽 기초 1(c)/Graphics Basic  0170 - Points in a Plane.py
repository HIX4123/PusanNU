from tkinter import *

W  = 800
H  = 800

def put_point(Can, x,y, color) :
    psize=7
    Can.create_oval(x,y, x + psize, y + psize, width=3, outline=color,fill=color)


master = Tk()
Mcan = Canvas(master, width= W, height= H )


P=[ [123, 345], [560,30], [400,130], [680,530]]
for w in P :
    x = w[0]
    y = w[1]
    print(f"x,y= {x,y}")
    put_point( Mcan, x, y, "red" )

#좌표를 float으로 해도 문제가 없다. 이것은 아주 편한 기능이다. 자동적으로 int 변환

P=[ [234.5, 34.5], [356,5,330.6], [490.5,530.567], [680,530]]
for w in P :
    x = w[0]
    y = w[1]
    print(f"x,y= {x,y}")
    put_point( Mcan, x, y, "black" )


Mcan.pack()
mainloop()
