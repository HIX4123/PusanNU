
class Table :
    def __init__(self): # 초기 생성자 (Constructor)
      self.person  = 0
      self.tea  = 4
      self.dish = 4

    def set_table(self, adult, child) :
        self.person = adult + child
        self.table = math.ceil( self.person/4.0)
        print("we preapred ", self.table, "Tables for ", self.person)

    def order(self, pizza, wine ) :
        self.pizza = pizza
        self.galicbread = (pizza+1)/2 * 2
        if wine == 0 : self.wine = 1
        else : self.wine = wine + 1

    def receipt(self) :
        self.food =  self.pizza*1.5 + self.galicbread/2*0.2 + self.wine*2.5
        self.tablecharge = self.person*0.3
        return(self.food + self.tablecharge)


t1 = Table()
t1.set_table(4,2)
t1.order(pizza=3, wine=2)
print(t1.receipt())
