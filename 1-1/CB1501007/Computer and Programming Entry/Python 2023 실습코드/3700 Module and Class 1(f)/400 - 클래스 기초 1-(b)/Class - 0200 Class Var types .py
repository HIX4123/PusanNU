
class Test:
    a = "a->"
    b = "b->"

    def __init__(self, a):
        print((self.a))
        self.a += a
        self._x = 123
        self.__y = 456 # 보호되는 변수
        b = 'meow'

    def touch( self ):
        self.a = self.a + "1000"
        self._x = self._x + 50000
        self.__y = self.__y - 10000
        self.a = self.a + "K"
        self.b = self.b + "C"

    def allout( self) :
        print(">>> In allout( ) <<< ")
        print((self.a))
        print((self.b))
        print((self._x))
        print((self.__y))


X = Test("44")
X.allout()

print((Test.a))
print((Test.b))
print((X.a))
print((X.b))
print((X._x))
#print X.__y

X.allout()
X.touch()
X.allout()
X.touch()
X.allout()