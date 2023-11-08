
# class24.py

class A(object):
    def save(self):
        print('A save called')

class B(A):
    pass

class C(A):
    def save(self):
        print('C save called')

class D(B, C):
    print("We called D")
    pass

d = D()
d.save()
