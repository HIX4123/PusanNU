
from PIL import Image
til = Image.new("RGB",(500,500), (100, 30, 220))
im = Image.open("dungdog.jpg") #25x25
im2 = Image.open("dungdog2.jpg")
im3 = im2.rotate( 45, expand=1)
til.paste(im, (0,0))
til.paste(im, (100,345))
til.paste(im,(0,150))
til.paste(im3,(230,123))
til.show()