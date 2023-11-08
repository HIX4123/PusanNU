

from tkinter import *
from   PIL import ImageFont
from   PIL import Image
from   PIL import ImageDraw

root = Tk()
root.title("CAPTCHAed Text")
root.geometry("500x500+300+300")

# font = ImageFont.truetype("Arial-Bold.ttf",14)
xfont= ImageFont.truetype("NanumMyeongjoBold.ttf",26)
img  = Image.new("RGBA", (300,250),(155,255,155))
draw = ImageDraw.Draw(img)
draw.text((50, 60), " 이것은 진짜 한글이다 \n 다음 문장",fill="black",font=xfont)
draw.line((10,20, 250,300), fill="black", width=2)
draw.line((10,20)+img.size, fill="red", width=2)
draw.line((210,80, 90,340), fill="black", width=2)
draw.arc((100,100,300,200),0,270,fill="green")

img.show()

root.mainloop( )
