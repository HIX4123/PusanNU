
from tkinter import *
from PIL import Image


im = Image.open("images/puppy6.jpg")

print("Format=", im.format)
print("Size= ", im.size)
print("Mode= ", im.mode)


im.show()

#root.mainloop( )