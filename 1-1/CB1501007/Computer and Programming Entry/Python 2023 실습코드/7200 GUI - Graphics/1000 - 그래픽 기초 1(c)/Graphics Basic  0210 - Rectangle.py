
#Tkinter -- Canvas의 사용법을 배웁니다.
# rectangle options
# http://infohost.nmt.edu/tcc/help/pubs/tkinter/web/create_rectangle.html

from tkinter import *
import math


def drawbox(P, xb,yb,xu,yu, mycolor):
    P.create_rectangle( xb,yb,xu,yu, fill=mycolor, width=1 )

N=500
root = Tk()
mycolor = "#%02x%02x%02x" % (250, 250, 250) # 256 흰색  0 검정색
mypaper = Canvas(root, width=N, height=N, background="Lightgreen")




drawbox( mypaper,  20, 30, 220, 230, mycolor)
mycolor = "#%02x%02x%02x" % (50, 220, 50)
drawbox( mypaper, 320, 230, 400, 370, mycolor)


mypaper.pack(fill=BOTH) #캔버스를 윈도우에 꽉차도록
root.mainloop()