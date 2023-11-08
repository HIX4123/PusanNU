

from tkinter import *   # Tkinter을 사용하기 위해 import
from PIL import Image, ImageTk   # 반드시 Tkinter 다음에 선언에야 한다.

root = Tk()
root.title( "Image 회전시키기")
root.geometry("400x400+300+300")

msize = 100, 100

source  = Image.open("church.jpg")
source2 = source.resize( (100,140) )
rot1 = source2.rotate( 140,   expand=1 )
target  = ImageTk.PhotoImage( rot1 )

mylabel = Label( root, image= target )
mylabel.place( x = 100 , y=100 )

root.mainloop( )