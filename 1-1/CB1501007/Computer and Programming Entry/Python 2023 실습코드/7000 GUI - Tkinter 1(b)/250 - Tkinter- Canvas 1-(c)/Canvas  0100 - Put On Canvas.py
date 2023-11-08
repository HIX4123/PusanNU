#-------------------------------------------------------------------------------
# Author:      Zoh
# Created:     2020-04-15
#-------------------------------------------------------------------------------

import tkinter

window=tkinter.Tk()
window.title("부산대학교 만세당")
window.geometry("500x400+100+100")
window.resizable(False, False)

canvas=tkinter.Canvas(window, relief="solid", bd=2 )

la = [10, 10, 20, 20, 20, 130, 30, 140 ]
lb = [ 150, 150, 270, 270, 300, 370 ]

line   = canvas.create_line   ( la , fill="red")
polygon= canvas.create_polygon( lb, outline="yellow")
oval   = canvas.create_oval   (100, 200, 150, 250, fill="blue", width=3)
arc    = canvas.create_arc    (100, 100, 300, 300, start=0, extent=150, fill='red')

canvas.pack()

window.mainloop()