
from PIL import Image

img = Image.open("church.jpg")
imbuffer = img.load()

print("이미지 크기 :", img.size)



pixels = img.load() # this is not a list, nor is it list()'able
width, height = img.size

all_pixels = []
for x in range( int(width/10)):
    for y in range( int(height/10)):
        cpixel = pixels[x, y]
        all_pixels.append(cpixel)


print(all_pixels)