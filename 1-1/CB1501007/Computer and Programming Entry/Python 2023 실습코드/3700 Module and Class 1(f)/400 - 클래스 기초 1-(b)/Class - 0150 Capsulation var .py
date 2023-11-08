

class Bread:
    def __init__(self):
        self.value = 0

    def decr(self):
        if self.value <= 0 : return
        self.value -= 1

    def incr(self):
        if self.value >= 4 :
            print("* no more")
            return
        self.value += 1  #

    def put(self):
        print(("현재값=", self.value))


# 어떤 변수, 0에서 4까지만 값을 가지도록 사용하고 싶다.
#

x = Bread()

x.put()
x.incr() ; x.put()
x.incr() ; x.put()
x.incr() ; x.put()
x.incr() ; x.put()
x.incr() ; x.put()
x.incr() ; x.put()