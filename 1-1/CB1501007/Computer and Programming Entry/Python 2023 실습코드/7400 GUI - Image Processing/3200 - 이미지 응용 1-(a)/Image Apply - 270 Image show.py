

from tkinter import *   # Tkinter을 사용하기 위해 import
from PIL import Image, ImageTk   # 반드시 Tkinter 다음에 선언에야 한다.

root = Tk()
root.title( "Image 보여주기 ")
root.geometry("600x600+300+300")

size = 100, 100

source  = Image.open("church.jpg")
target  = ImageTk.PhotoImage( source )

mylabel = Label( root, image= target )
mylabel.place( x = 100 , y=100 )

root.mainloop( )