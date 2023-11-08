

from PIL import Image

img = Image.open("rainnyday.jpg")
print ("Image size = ", img.size)
X= int(input("Type X :"))
Y= int(input("Type Y :"))
print (img.getpixel((X, Y)))

print ("X=", X)


box = (X, Y, X+400, Y+400) #변수 box에 자를 좌표 넣기 (x0, y0, x1, y1)
croppedbox = img.crop(box) #box를 자르는 함수인 crop의 인자에 넣는다.
croppedbox.save("croppedimg.jpg") #자른 내용 저장하기