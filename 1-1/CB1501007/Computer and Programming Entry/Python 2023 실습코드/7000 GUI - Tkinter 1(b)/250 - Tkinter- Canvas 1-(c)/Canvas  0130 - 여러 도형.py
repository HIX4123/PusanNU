import tkinter as tk
from random import randint

def circle():
    x = randint(0, 799)
    y = randint(0, 799)
    diameter = randint(10, 400)
    canvas.create_oval(x, y, x + diameter, y + diameter)


def rectangle():
    x = randint(0, 799)
    y = randint(0, 799)
    canvas.create_rectangle(x, y, x + randint(10, 100), y + randint(10, 100))


def text():
    x = randint(0, 799)
    y = randint(0, 799)
    canvas.create_text(x, y, text=f"x={x}, y={y}")


window = tk.Tk()
window.title("Drawing Shapes on Button Press")
window.geometry("1000x800")
canvas = tk.Canvas(width=1000, height=800)
canvas.pack()

circle( )
rectangle( )
text( )
window.mainloop( )