

def make_adder(n):  # return function
    def add(x):
        return x + n
    return add

class Adder:
    def __init__(self,n):
        self.n = n
    def __call__(self, x):
        return( self.n + x)


plus3 = make_adder(3)
w = plus3(100)

print("w =", w)

plus55 = Adder(55)
w = plus55(500)
print("w =", w)