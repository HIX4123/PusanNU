
from tkinter import *
from PIL import Image


im = Image.open("images/puppy5.jpg")

print("Format=", im.format)
print("Size= ", im.size)
print("Mode= ", im.mode)


print("좌표(100,100)의 pixel값 = ", im.getpixel( (100, 100) ))
# (R,G,B,A) A는 투명도 조정.
im.putpixel( (5,5), ( 255, 255, 255, 255) )
im.putpixel( (6,5), ( 255, 255, 255, 10) )
im.putpixel( (7,5), ( 255, 255, 255, 20) )
im.putpixel( (8,5), ( 255, 255, 255, 30) )
im.putpixel( (9,5), ( 255, 255, 255, 50) )

im_raw = im.load()
print("im_raw[5,5]=", im_raw[5,5])  # 전체를 pixel buffer로 만듬.
im_raw[10,5] = ( 255, 0, 0, 255)
im_raw[10,6] = ( 255, 0, 0, 255)
im_raw[10,7] = ( 255, 0, 0, 255)
im_raw[10,8] = ( 255, 0, 0, 255)
im_raw[10,9] = ( 255, 0, 0, 255)
im_raw[10,10] = ( 255, 0, 0, 255)
im_raw[10,11] = ( 255, 0, 0, 255)

print(im.getpixel((9,5)))

#im.save("images/saved2018.jpg")
im.show()

#root.mainloop( )