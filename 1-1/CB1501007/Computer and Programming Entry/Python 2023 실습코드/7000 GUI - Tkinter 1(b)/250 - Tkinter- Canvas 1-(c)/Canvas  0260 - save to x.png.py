#-------------------------------------------------------------------------------
# Purpose:     2020 Prof. Zoh's Work
# Author:      Cho
# Created:     2020-09-02
#-------------------------------------------------------------------------------

# 반드시 Ghostscript가 system path에 연결되어야 한다.
# GhostScript 9.52를 새로 설치하였음. 2020

import numpy
import math
import random
import tkinter as tk
from   PIL import Image, ImageTk, ImageDraw, ImageGrab


root = tk.Tk()
root.title("Simple plot")

cv = tk.Canvas(width=500, height=500, bg='white')
cv.pack()

cv.create_text(100, 100, font=("Courier New",17), text="Will Will We Win!")
cv.create_rectangle(150, 170, 300, 300, fill="lightgreen"  )
cv.update() # comment out to make empty postscript!

cv.postscript(file="zoh_drawing.ps", colormode='color')

def save_canvas( root, canvas, filename ):
    x = root.winfo_rootx() + canvas.winfo_x()
    y = root.winfo_rooty() + canvas.winfo_y()
    xx = x + canvas.winfo_width()
    yy = y + canvas.winfo_height()
    print(f"x,y,xx,yy={x,y,xx,yy}")
    ImageGrab.grab(bbox=(x, y, xx, yy)).save(filename)
    return

save_canvas( root, cv, "Zoh-2023D.png")

root.mainloop( )