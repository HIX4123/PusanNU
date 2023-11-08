#-------------------------------------------------------------------------------
# Purpose:     2019 Power Python
# Author:      Cho
#-------------------------------------------------------------------------------


from tkinter import *
import tkinter.font

root = tkinter.Tk()
canvas = tkinter.Canvas(root, width=400, height=400, background="bisque")
canvas.pack(fill="both", expand=True)

normal_font = tkinter.font.Font(family="Helvetica", size=15)
out_font    = tkinter.font.Font(family="Helvetica", size=15, weight="bold", overstrike=True)
bold_font   = tkinter.font.Font(family="Helvetica", size=15, weight="bold" )

canvas.create_text( 50, 50, text="This is normal",  font=normal_font)
canvas.create_text( 50,100, text="This is bold",    font=bold_font )
canvas.create_text(150,130, text="This is a bad text for you", \
                   font=out_font )

root.mainloop()