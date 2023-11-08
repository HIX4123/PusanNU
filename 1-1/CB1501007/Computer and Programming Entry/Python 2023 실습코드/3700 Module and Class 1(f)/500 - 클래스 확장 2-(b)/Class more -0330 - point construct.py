

class Point:
   def __init__( self, x=0, y=0): # 초기값 지정하기
      self.x = x
      self.y = y

   def __del__(self):
      class_name = self.__class__.__name__
      print(class_name, "destroyed")

   def printpoint(self) :
        print(self.x, self.y)

pt1 = Point(23, 45)
pt2 = pt1
pt3 = pt1
pt3 = Point(-1,-1)
print("pt1=", id(pt1), "pt1=",id(pt2), "pt1=",id(pt3)) # prints the ids of the obejcts


pt1.printpoint()
pt3.printpoint()
#pt2.printpoint() #이렇게 하면 오류가 발생한다.

del pt1
del pt2
del pt3