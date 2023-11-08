
class Box :
    def __init__(self, x, y ):
        self.black = x
        self.white = y

    def getout(self) :
        if self.black >= 4 : self.black -= 4
        if self.white >= 3 : self.white -= 3

    def putinto(self) :
        self.black += 2
        self.white += 4

    def showBox(self) :
        print("(%2d, %2d)" % (self.black, self.white))


mybin = Box(30, 30)
mybin.showBox()
mybin.getout()
mybin.putinto()
mybin.showBox()

# 여러분은 black ball을 31개로 만들 수 없다. 이 변수는 method( )에
# 의해서 완전히 감추어져(encapsulation)쌓여져 있기 때문이다.

class JustCounter:
   __secretCount = 0  # Class 외부 사용자가 사용할 수 없는 함수

   def count(self):
      self.__secretCount += 1
      print(self.__secretCount)

counter = JustCounter()
counter.count() ; counter.count()
counter.count() ; counter.count()
#print counter.__secretCount  #이것울 불가능하도록 만들어 준다.
