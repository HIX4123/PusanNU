
from tkinter import *   # tkinter을 사용하기 위해 import
from PIL import Image, ImageTk  # 반드시 tkinter 다음에 선언에야 한다.
from   PIL import ImageFont
from   PIL import Image
from   PIL import ImageDraw
from   PIL import ImageTk

root = Tk()
root.title( "Image 회전시키기")
root.geometry("600x700+300+300")


src_im  = Image.open("church.jpg")
iobj    = ImageTk.PhotoImage( src_im )
mylabel = Label( root, image=iobj)
mylabel.place( x = 100 , y=100 )

src_im.save("Krotate.png")
root.mainloop( )