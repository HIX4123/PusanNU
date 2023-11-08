
class myObj:
   name = "John"

class Vehicle:
    pass

class Truck(Vehicle):
    pass



w = myObj( )

la = [ 10, 10.5 , True, "Good", [3,4,5], w, Truck, Vehicle ]

for x in la :
    print(type(x))


print("exp1= ", isinstance(Vehicle(), Vehicle))  # returns True
print("exp2= ", type(Vehicle()) == Vehicle)      # returns True
print("exp3= ", isinstance(Truck(), Vehicle))    # returns True
print("exp4= ", type(Truck()) == Vehicle)        # returns False, and this probably won't be what you want.
