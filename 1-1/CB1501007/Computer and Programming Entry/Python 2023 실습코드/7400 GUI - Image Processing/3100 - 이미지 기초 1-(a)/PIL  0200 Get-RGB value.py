
from PIL import Image

img = Image.open("church.jpg")
imbuffer = img.load()

print("이미지 크기 :", img.size)

rgb_img = img.convert('RGB')
r, g, b = rgb_img.getpixel((1, 1)) ; print(r, g, b)
r, g, b = rgb_img.getpixel((199, 100)) ; print(r, g, b)
