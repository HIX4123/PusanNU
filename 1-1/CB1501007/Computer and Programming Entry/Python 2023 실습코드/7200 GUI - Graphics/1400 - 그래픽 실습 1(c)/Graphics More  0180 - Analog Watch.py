
from tkinter import *
import math


root = Tk()
mycolor = "#%02x%02x%02x" % (250, 250, 250) # 256 흰색  0 검정색

N=500
mypaper = Canvas(root, width=N, height=N, background="Lightgreen")
mypaper.grid(row=0, column=0)  #캔버스를 윈도우에 꽉차도록

R=200
theta=0.0
mypause = 1000  # 1000ms
delta = 2*math.pi/ 60.0
for x in range(100) :
    theta = theta + delta
    tick= mypaper.create_line( N/2, N/2,\
                         R*math.cos(theta)+N/2,\
                         R*math.sin(theta)+N/2, \
                         fill="red" , width=3 )

    mypaper.update()           # 캔버스 위에 새로 고쳐서 그린다.
    mypaper.after( mypause )   # 1000ms 실행 일시 정지
    mypaper.delete( tick )
#    mypaper.delete( ALL )
    print('theta= ', theta)



root.mainloop( )