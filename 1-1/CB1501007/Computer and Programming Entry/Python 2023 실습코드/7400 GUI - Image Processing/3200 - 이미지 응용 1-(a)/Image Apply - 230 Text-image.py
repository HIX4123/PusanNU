
import PIL
from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw

# font = ImageFont.truetype("Arial-Bold.ttf",14)
myfont   = ImageFont.truetype("Arial.ttf",24)
yourfont = ImageFont.truetype("Calibri.ttf",24)
img=Image.new("RGBA", (500,250),"orange")
draw = ImageDraw.Draw(img)
draw.text((100, 70),"This is a test",(0,0,0),font=myfont)
draw.text((100, 140),"Summer Time Blues, \n My Blues",(0,0,0),font=myfont)
draw = ImageDraw.Draw(img)

img.show()
#img.save("a_test.png")
