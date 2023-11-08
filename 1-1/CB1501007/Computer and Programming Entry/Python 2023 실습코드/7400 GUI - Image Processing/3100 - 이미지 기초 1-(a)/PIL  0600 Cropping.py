
from PIL import Image

img = Image.open("church.jpg")
imbuffer = img.load()

print("이미지 크기 :", img.size)

X=eval(input("X"))
Y=X
offset=150
print("RGB :", img.getpixel((X, Y))) #픽셀의 RGB값을 출력한다.


box = (X, Y, X+offset, Y+offset ) #변수 box에 자를 좌표 넣기 (x0, y0, x1, y1)
croppedbox = img.crop(box) #box를 자르는 함수인 crop의 인자에 넣는다.

croppedbox.show()
#croppedbox.save("croppedimg.jpg") #자른 내용 저장하기

print("croppedimg.jpg 파일에 저장완료")

