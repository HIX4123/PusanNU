
from tkinter import *
from PIL import Image, ImageTk, ImageDraw

width = 400
height = 300
center = height//2
white = (255, 255, 255)
green = (0,128,0)

root = Tk()
root.geometry("600x600+500+500")  # 크기와 window가 처음 놓일 위치

# Tkinter create a canvas to draw on
cv = Canvas(root, width=width, height=height, bg='white')
cv.pack()

# PIL create an empty image and draw object to draw on memory only, not visible
image1 = Image.new("RGB", (width, height), white)
draw = ImageDraw.Draw(image1)

# do the Tkinter canvas drawings (visible)
cv.create_line([0, center, width, center], fill='green')
cv.create_text( 130, 130, text="Good Move")

# do the PIL image/draw (in memory) drawings
draw.line([0, center, width, center], green)


# PIL image can be saved as .png .jpg .gif or .bmp file (among others)
filename = "Zoh-2023.jpg"
image1.save(filename)

root.mainloop()