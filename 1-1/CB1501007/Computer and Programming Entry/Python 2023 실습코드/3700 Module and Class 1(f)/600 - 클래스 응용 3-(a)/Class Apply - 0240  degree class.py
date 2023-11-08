
# class16.py

class D(object):
        def __init__(self):
                self.__degree = 0
        def get_degree(self): 	#
                return self.__degree
        def set_degree(self, d): 	#
                self.__degree = d % 360
#        degree = property(get_degree, set_degree) #

d = D()
d.degree = 10
print("Out1= ", d.degree)
d.degree = 370
print("Out2= ", d.degree)
d.degree = -370
print("Out3= ", d.degree)
