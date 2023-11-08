# see this page http://effbot.org/imagingbook/introduction.htm


from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.geometry("500x480+300+300")

myimg = Image.open("kota.jpg")
imobject = ImageTk.PhotoImage( myimg )

mylabel = Label( root, image=imobject )
mylabel.grid( row=1000, column=1000)
mylabel.grid( row=2000, column=2000)


root.mainloop();

