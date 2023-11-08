#-------------------------------------------------------------------------------
# Purpose:     2020 컴퓨터및 프로그래밍 입문
# Author:      Cho
# Created:     2020-04-16
#-------------------------------------------------------------------------------


from tkinter import *
from PIL import Image, ImageDraw


width  = 400
height = 300
center = height//2
white  = (255, 255, 255)
green  = (0,128,0)

root = Tk()


cv = Canvas(root, width=width, height=height, bg='white')
cv.pack()

# PIL create an empty image and draw object to draw on memory only, not visible
image1 = Image.new("RGB", (width, height), white)
draw = ImageDraw.Draw(image1)

cv.create_line([0, center, width, center+20], fill='green', width=3)

# do the PIL image/draw (in memory) drawings
draw.line([0, center, width, center], green, width=2 )

# PIL image can be saved as .png .jpg .gif or .bmp file (among others)
filename = "my_drawing.jpg"
image1.save(filename)

root.mainloop()