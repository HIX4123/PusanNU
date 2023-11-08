
import random

class Land :
    land="" ;  count = 0 ;  bits = 0 ;  limit = 0
    def __init__(self):
        #random.seed(2016)
        print("oh We mad a land")
        self.s = random.randint(1,20)
        self.p = random.randint(1,30)
        self.q = random.randint(1,20)
        self.land = self.s*"0"+ self.p*"1" + self.q*"0"
        print(self.land)
        self.limit = 5

    def ask(self, a,b):
        self.count += 1
        if self.count > self.limit :
            print("Overflow")
            exit(0)
        self.bits=0
        for x in self.land[a:b+1] :
            if x == "1" : self.bits += 1

        if self.bits == (b-a+1) :
            return 2
        elif self.bits >= 1 :
            return 1
        else : return 0

    def showcount(self):
        return self.count





X = Land()

print(X.ask(8,13))
print(X.ask(0,5))
print(X.ask(8,13))
print(X.ask(0,5))
print("Count=", X.showcount())
