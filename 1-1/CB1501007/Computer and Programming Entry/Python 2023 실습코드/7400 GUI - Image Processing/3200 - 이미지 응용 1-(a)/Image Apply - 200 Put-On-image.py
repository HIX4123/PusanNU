
from tkinter import *   # tkinter을 사용하기 위해 import
from PIL import Image, ImageTk  # 반드시 tkinter 다음에 선언에야 한다.
from   PIL import ImageFont
from   PIL import Image
from   PIL import ImageDraw


root = Tk()
root.title("Vision and Vision")
root.geometry("900x980+300+300")

img     =   Image.open("church.jpg")
newim   =   Image.new("RGB",(256,256),(102,153,255))
pix     =   img.load()
pix[100,100]=(0,0,0)
pix[101,101]=(0,0,0)
pix[102,102]=(0,0,0)
pix[103,103]=(0,0,0)

print("이미지 크기 :", img.size)
print("RGB :", img.getpixel((0, 0))) #픽셀의 RGB값을 출력한다.


img.show()
#iobj = ImageTk.PhotoImage( img )
#mylabel = Label( root, image=iobj)
#mylabel.place( x = 100 , y=100)

#root.mainloop( )

# 단색 이미지 만들기
