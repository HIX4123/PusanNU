
def ListSuperClasses(classInstance, clist=None):
    if not clist: clist = []
    for klass in classInstance.__bases__:
        clist.append(klass.__name__)    # ?대쫫留뚯쓣 痍⑦븯湲곕줈 ?섏옄
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

def getAttribute(klass, attr=None):
        if attr == None:
                attr = []
        for k in klass.__bases__:
                getAttribute(k, attr)
        for a in dir(klass):
                if a not in attr:
                        attr.append(a)
        return attr

#
print('Attributes of Super1=', getAttribute(Super1))
print('Attributes of Sub=', getAttribute(Sub))
