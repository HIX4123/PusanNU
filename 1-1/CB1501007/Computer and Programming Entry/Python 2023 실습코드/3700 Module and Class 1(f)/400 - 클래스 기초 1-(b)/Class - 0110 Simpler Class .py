

class X :
    def __init__(self, a):
        self.name= a

    def assign(self,b):
        self.name = b

    def mo(self,c) :
        x = X("None")
        x.assign( self.name+" Foo")
        return x

    def out(self):
        print(("Name=", self.name))


Q = X("book")
Q.out()
Q.assign("V")
M = Q.mo("cool")
M.out()


