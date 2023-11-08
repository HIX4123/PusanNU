
class A:
        pass

class B:
        def f(self):
                pass

class C(B):
        pass

def check(obj):
        print(obj, '=>', end=' ')
        if issubclass(obj, A): print('A', end=' ')
        if issubclass(obj, B): print('B', end=' ')
        if issubclass(obj, C): print('C', end=' ')
        print()

check(A)
check(B)
check(C)
