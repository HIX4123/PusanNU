
class A:
        pass

class B:
        def f(self):
                pass

class C(B):
        pass

def check(obj):
        print(obj, '=>', end=' ')
        if isinstance(obj, A): print('A', end=' ')
        if isinstance(obj, B): print('B', end=' ')
        if isinstance(obj, C): print('C', end=' ')
        print()

a = A()
b = B()
c = C()

check(a)
check(b)
check(c)
