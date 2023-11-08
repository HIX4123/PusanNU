#-*- coding: cp949 -*-
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



class myCircle:
    def __init__(self, x,y, d):
        self.ox = x
        self.oy = y
        self.diameter = d

    def __add__(self, yourC ):
        self.ox = (self.ox + yourC.ox)/2
        self.oy = (self.oy + yourC.oy)/2
        self.diameter = self.diameter + yourC.diameter

    def info( self ) :
        print("(", self.ox, ",", self.oy, ")" )
        print ("diameter=", self.diameter)



a = myCircle( 9,10, 30 )
b = myCircle(17,50, 13 )
a.info( )

a + b #  a원에 b원을 더한다.

a.info( )

