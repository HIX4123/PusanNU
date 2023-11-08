
import PIL
from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw

engfont = ImageFont.truetype("arial.ttf", 34)
korfont= ImageFont.truetype("NanumMyeongjo.ttf",24)
im = Image.new("RGB", (300, 300), (100,120, 180))
draw = ImageDraw.Draw(im)

#          위치       문자      색상      폰트와 크기
draw.text((50, 50), "Hey U!", (255,0,0),  font= engfont)
draw.text((50, 150), "이건 뭐여", (255,0,0),  font= korfont)

im.rotate(180).show()  #이미지 전체를 뒤집는다


