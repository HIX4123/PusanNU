#-*- coding: cp949 -*-
# class33.py

def ListSuperClasses(classInstance, clist=None):
    if not clist: clist = []
    for klass in classInstance.__bases__:
        clist.append(klass.__name__)    #
        ListSuperClasses(klass, clist)
    return clist

class Super1:
        m1 = 1
        def a(self):
                pass
        def b(self):
                pass

class Super2(Super1):
        m2 = 2
        def c(self):
                pass
        def d(self):
                pass

class Super3(Super1):
        m2 = 2
        def c(self):
                pass
        def d(self):
                pass

class Sub(Super2, Super3):
        m3 = 3
        m4 = 4
        def x(self): pass
        def y(self): pass

print(ListSuperClasses(Sub))  #
s = Sub()
print(ListSuperClasses(s.__class__)) #
