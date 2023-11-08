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

canvas = Canvas(width=800, height=800)
canvas.pack()

root.title("Transparent rectangle Making")

create_rectangle( 10,  10, 400, 400, fill='blue',    alpha=.4)
create_rectangle(250, 250, 650, 550, fill='green',   alpha=.2)
create_rectangle(180, 280, 450, 320, fill='#800000', alpha=.2)

root.mainloop()