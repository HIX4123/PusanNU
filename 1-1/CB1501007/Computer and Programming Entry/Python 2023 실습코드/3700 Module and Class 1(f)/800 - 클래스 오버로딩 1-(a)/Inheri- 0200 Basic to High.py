
class basic:
    cream = "clinique"  # Class member
    skin = "amore"
    def __init__(self): # 생성될 때 자동으로 수행되는 method
        self.lipstick  = "Null"  #Instance Member
    def totalprice(self) :
        return (10000)
    def info(self):
        print (self.cream, self.skin, self.lipstick , "<---")

class high(basic):
    compact = "krio"
    def totalprice(self) :
        return (45000)
    def info(self):
        basic.info(self)
        print (self.compact , "<---")
    def moreinfo(self):
            self.info()
            print ("2개를 구입하면 하나는 공짜 제공")
    def __del__(self):
        print ("ITEM was destroyed from our program")


A = basic()
B = basic()
C = high()
A.info()
C.info()
C.moreinfo()

print ("\n Class 내부의 변수 출력해보기")
print (C.cream)
print (C.skin)
C.lipstick = "MuchMore"
print (C.lipstick)
del(C)    # 보통의 경우에는 시스템이 알아서 해준다. 아주 큰 경우가 아니라면
