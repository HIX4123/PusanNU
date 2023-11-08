# Purpose:
# 연산자 겹치기(overloading)이란 사용자가 편의대로
# 활용할 수 있도록 해주는 매우 편리한 기능이다.

# __add__(self, other)          +               A + B, A += B
# __pos__(self)                 +               +A
# __sub__(self, other)          -               A - B, A -= B
# __neg__(self)                 -               -A
# __mul__(self, other)          *               A * B, A *= B
# __truediv__(self, other)      /               A / B, A /= B
# __floordiv__(self, other)    //               A // B, A //= B
# __mod__(self, other)          %               A % B, A %= B
# __pow__(self, other) pow(),  **               pow(A, B), A ** B
# __lshift__(self, other)      <<               A << B, A <<= B
# __rshift__(self, other)      >>               A >> B, A >>= B
# __and__(self, other)          &               A & B, A &= B
# __xor__(self, other)          ^               A ^ B, A ^= B
# __or__(self, other)           |               A | B, A |= B
# __invert__(self)              ~              ~A
# __abs__(self)             abs()               abs(A)

# Less than             p1 < p2 p1      .__lt__(p2)
# Less than or equal to p1 <= p2 p1     .__le__(p2)
# Equal to              p1 == p2 p1     .__eq__(p2)
# Not equal to p1       != p2 p1        .__ne__(p2)
# Greater than          p1 > p2 p1      .__gt__(p2)
# Greater or equal to   p1 >= p2 p1     .__ge__(p2)



class MyString:
    def __init__(self, str):
        self.str = str
        self.ans = ""
    def __truediv__(self, sep):     # 나눗셈을 정의할 수 있다.
        print (self.str, sep )
        self.ans = self.str.split(sep)      # 결과값을 돌려준다.
        return ( self.ans )
    def __neg__(self):
        t = list(self.str)
        t.reverse()
        return ''.join(t) # t를 return하면 하나의 list만 돌아간다.
                          # 각 원소는 공백없이 붙혀라.
    def info( self ) :
        print("self.str=", self.str, "self.ans=", self.ans )
# ----------- Overloading Class -----------

m = MyString("abcdabcdabcd")
m.info()
print(m/"b")   # b롤 분리한 결과를 돌려준다.
print (m/"bc"  )    #
print (-m)

