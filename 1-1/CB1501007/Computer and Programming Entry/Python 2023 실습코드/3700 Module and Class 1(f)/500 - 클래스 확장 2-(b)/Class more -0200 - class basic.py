
class Book:
    def setprice(self, v):
        self.price = v
    def makecover( self, title) :
        self.title = title
    def putprice(self):
        print(self.price)

class Mobile:
    def set(self, v):
        self.price = v
    def used(self):
        self.set(self.price - 1)  # Class 내부의 값을 +1 증가 시킨다.
    def putprice(self):
        print(self.price)

class Comm:
    c_mem = 100         #
    def f(self):
        self.i_mem = 200        #
    def g(self):
        print(self.i_mem)
        print(self.c_mem)


A = Book() # Book Class로 어떤 복합변수를 만듬.
B = Mobile() # Mobile Class의 이름 공간이 생김.

Book.version = 2       # Book의 이름공간에 새로운 변수 창출
Mobile.version = 100   # version 같은 변수이지만 이름 공간이 다름.
Book.price = 99

A.price = 15000         # A는 클래스 Book의 instnace, 그것을 instance화
B.price = 8900

Tlist=[A, B]
print("Tlist=", Tlist[0].price)
print("type(A)=", type(A))

