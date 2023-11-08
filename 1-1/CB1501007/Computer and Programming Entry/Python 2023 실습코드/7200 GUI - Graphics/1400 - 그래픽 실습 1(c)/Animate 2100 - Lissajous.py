
from tkinter import*
import math

root=Tk()

width = 500
height = 500

vcenter = height/2
hcenter = width/2

y_amplitude = 100

canvas = Canvas(root, width=width, height=height, bg='white')
canvas.pack(side='left')

canvas.create_line(hcenter, 0, hcenter, height)
canvas.create_line(0, vcenter, width, vcenter)

def lissajous(t):
    x= 2*math.cos(10*math.pi*t)*y_amplitude + vcenter
    y= 1*math.sin(20*math.pi*t)*y_amplitude + vcenter
    return ((x,y))

t=0
delta=1.0/1000
prev_w, prev_v=lissajous(t)

for i in range(1000):
    t=t+delta
    w, v = lissajous(t)
    line=canvas.create_line(prev_w, prev_v, w, v, fill='red')
    prev_w, prev_v = w, v

root.title("Lissajous")
root.mainloop()