
class Parent:
     def mustMake(self):
         raise NotImplementedError

class Child(Parent):
     def mustMake(self):
         print("mustMake() is made by Child class")

a = Child()
a.mustMake()

b = Parent()
#b.mustMake()



# 출처: http://agiantmind.tistory.com/39 [Warehouse B]