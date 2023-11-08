#-*- coding: cp949 -*-
# Overloading을 이용해서 크기 비교를 해봅니다.

class Point:
      def __init__(self,x = 0,y = 0):
        self.x = x
        self.y = y

      def __lt__(self,other):
        self_mag = (self.x ** 2) + (self.y ** 2)
        other_mag = (other.x ** 2) + (other.y ** 2)
        return self_mag < other_mag


print ("a=", Point(1,1) < Point(-2,-3))

print ("b=",Point(1,1) < Point(0.5,-0.2))

print ("c=",Point(1,1) < Point(1,1))


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


