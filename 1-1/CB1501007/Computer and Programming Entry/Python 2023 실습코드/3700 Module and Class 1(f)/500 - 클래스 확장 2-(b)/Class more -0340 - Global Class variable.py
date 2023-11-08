
class cookie :
      def __init__(self,this):
        global dodo    # 사실은 이렇게 밖으로 열어주면 안됩니다.
        self.name= this
        dodo = "과자="+this



class book :
      def __init__(self,this):
        self.name= this


def classfun ( mybook, mycookie ):
    print(mybook.name , " 책을 읽으면서 ", mycookie.name , "을 먹읍시다")

banana = cookie( "바나나칩")
b      = cookie("땅콩")
mang   = book("맹자")
d      = book("논어")

print(b.name, d.name)  # 이렇게 class global 변수는 호출 가능함.
classfun( mang,banana )