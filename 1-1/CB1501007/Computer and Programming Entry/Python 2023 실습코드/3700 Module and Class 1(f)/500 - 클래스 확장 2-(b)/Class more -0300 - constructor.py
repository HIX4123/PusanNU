
class mobile:
    def __init__(self): # 생성될 때 자동으로 수행되는 method
        self.made  = "Null"
        self.price = 0
        self.base  = 0
        print("우리는 mobile data를 새롭게 생성했습니다")

    def firstbuy(self, company, cost, base ):
        self.made  = company
        self.price = cost
        self.base  = base
    def info( self):
        print(self.made, self.price, self.base)


class smart(mobile): # Class는 상속이 됩니다.
    def __init__(self): # 생성될 때 자동으로 수행되는 method
        self.made  = "Uganda"
        self.price = 1000000
        self.base  = 9999
        self.os    = "WinCE"
    def setos(self, ostype):
        self.os = ostype

    def info( self ):
        print(self.made, self.price, self.base, self.os)


thisphone = mobile()
yourphone = mobile()
print("\n 실험1: 초기에 생성만 한 경우")
gift = smart()
thisphone.info()
yourphone.info()
gift.info()

print("\n 실험2: 실제 예를 만들 경우(instance만들기)")
thisphone.firstbuy("LG", 230000, 20000)
yourphone.firstbuy("SS",      0, 59000)
thisphone.info()
yourphone.info()

print("\n 실험3: 실제 스마트폰의 예를 만들기")
gift.firstbuy("Apple", 850000, 50000)
gift.setos("ANDROID")
gift.info()


