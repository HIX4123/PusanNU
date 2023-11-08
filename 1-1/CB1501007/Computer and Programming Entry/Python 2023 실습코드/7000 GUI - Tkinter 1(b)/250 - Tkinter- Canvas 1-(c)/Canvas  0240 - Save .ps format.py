#-------------------------------------------------------------------------------
# Purpose:     2020 Prof. Zoh's Work
# Author:      Cho
# Created:     2020-09-02
#-------------------------------------------------------------------------------

# 반드시 Ghostscript가 system path에 연결되어야 한다.
# GhostScript 9.52를 새로 설치하였음. 2020


import tkinter as tk

root = tk.Tk()
root.title("Simple plot")

cv = tk.Canvas(width=500, height=500, bg='white')
cv.pack()

cv.create_text(100, 60, text="hello world!")
cv.create_rectangle(100, 100, 300, 300, fill="green"  )

# 반드시 넣어  주어야 함.
cv.update() # comment out to make empty postscript!

cv.postscript(file="zoh_drawing.ps", colormode='color')


root.mainloop( )