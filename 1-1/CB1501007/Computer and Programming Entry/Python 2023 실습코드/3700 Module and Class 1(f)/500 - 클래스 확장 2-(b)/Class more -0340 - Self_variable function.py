
class cookie :
      def __init__(self,this):
        self.name= this

class book :
      def __init__(self,this):
        self.name= this


def classfun ( mybook, mycookie ):
    print(mybook.name , " 책을 읽으면서 ", mycookie.name , "을 먹읍시다")

banana = cookie( "바나나칩")
b      = cookie("땅콩")
mang   = book("맹자")
d      = book("논어")

print(b.name, d.name)  # 이렇게 class 내부 변수를 부를 수는 있지만
b.name = "막걸리"
classfun( mang,banana )