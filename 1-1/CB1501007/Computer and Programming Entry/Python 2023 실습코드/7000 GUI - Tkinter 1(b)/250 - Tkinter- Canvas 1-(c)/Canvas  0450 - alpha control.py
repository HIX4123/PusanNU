#-------------------------------------------------------------------------------
# Author:      Zoh
# Created:     2020-04-15
#-------------------------------------------------------------------------------

from tkinter import *
from PIL import Image, ImageTk

root = Tk()

images = []  # to hold the newly created image

def create_rectangle(x1, y1, x2, y2, **kwargs):
    if 'alpha' in kwargs:
        alpha = int(kwargs.pop('alpha') * 255)
        fill = kwargs.pop('fill')
        fill = root.winfo_rgb(fill) + (alpha,)
        image = Image.new('RGBA', (x2-x1, y2-y1), fill)
        images.append(ImageTk.PhotoImage(image))
        canvas.create_image(x1, y1, image=images[-1], anchor='nw')
    canvas.create_rectangle(x1, y1, x2, y2, **kwargs)

canvas = Canvas(width=600, height=700)
canvas.pack()

create_rectangle( 10,  10, 400, 400, fill='blue'             )
create_rectangle( 50,  50, 550, 350, fill='green',   alpha=.5)
create_rectangle(280, 280, 650, 620, fill='#800000', alpha=.2)

root.mainloop()