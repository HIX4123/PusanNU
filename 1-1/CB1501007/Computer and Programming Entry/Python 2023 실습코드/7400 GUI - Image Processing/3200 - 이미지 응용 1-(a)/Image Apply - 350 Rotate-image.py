
from PIL import Image

src_im = Image.open("church.jpg")
angle = 45
size = 100, 100

dst_im = Image.new("RGBA", (300,300), (100,120,180) )
im = src_im.convert('RGBA')
rot1 = im.rotate( angle, expand=1 ).resize(size)
rot2 = im.rotate( angle*3, expand=1 ).resize(size)
dst_im.paste( rot1, (50, 50), rot1 )
dst_im.paste( rot2, (150, 150), rot2 )
dst_im.show()