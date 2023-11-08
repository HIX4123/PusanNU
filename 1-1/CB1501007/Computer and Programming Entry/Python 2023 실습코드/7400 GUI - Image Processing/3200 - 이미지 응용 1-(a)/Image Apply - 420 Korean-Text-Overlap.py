
from PIL import Image, ImageFont, ImageDraw

text = '착하게 살자. 항상'
font = ImageFont.truetype('NanumMyeongjo.ttf', 50)
width, height = font.getsize(text)

bcolor = (0, 128, 0 ) # ),92)
tcolor = (255, 128, 0)
mcolor = (10, 90, 200)
image1 = Image.new('RGBA', (500, 500), bcolor )
draw1 = ImageDraw.Draw(image1)
draw1.text((40, 90), text=text, font=font, fill= tcolor )

image2 = Image.new('RGBA', (width, height), (0, 0, 128, 0))
#                                                      alpha=0 투명
draw2 = ImageDraw.Draw(image2)
draw2.text((0, 0), text=text, font=font, fill= mcolor )
image2 = image2.rotate(180, expand=1)

px, py = 10, 10
sx, sy = image2.size
#image1.paste(image2, (px, py, px + sx, py + sy), image2)
image1.paste(image2, (40, 90), image2)

image1.show()