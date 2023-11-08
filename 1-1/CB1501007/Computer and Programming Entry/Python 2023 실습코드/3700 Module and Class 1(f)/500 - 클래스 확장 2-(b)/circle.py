
# 고친 다음에는 수행을 시켜야 python system에서 기억해둔다.

class Circle :
    cx = cy = 0
    diameter= 0
    def __init__(self, x, y, r):
        self.cx = x
        self.cy = y
        self.diameter = r
        if r <= 0 :
            print("Construction Error: Negative length")
            exit(0)

    def area(self):
        return 3.1415924*self.diameter**2

    def center(self):
        return (self.cx, self.cy)

    def inout(self, x,y):
        self.leng = (self.cx - x)**2 +(self.cy - y)
        if self.leng**2 < self.diameter**2 :
            return "in"
        else : return "out"


