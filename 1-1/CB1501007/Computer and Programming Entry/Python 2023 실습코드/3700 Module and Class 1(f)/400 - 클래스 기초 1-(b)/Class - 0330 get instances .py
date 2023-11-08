

from collections import defaultdict
import weakref

class KeepRefs(object):
    __refs__ = defaultdict(list)
    def __init__(self):
        self.__refs__[self.__class__].append(weakref.ref(self))

    @classmethod
    def get_instances(cls):
        for inst_ref in cls.__refs__[cls]:
            inst = inst_ref()
            if inst is not None:
                yield inst

class X(KeepRefs):
    def __init__(self, name):
        super(X, self).__init__()
        self.name = name

x = X("x")
y = X("y")
banana=X("banana")
apple=X("apple")

for r in X.get_instances():
    print(r.name, end=', ')

del y, apple
print("\n\n after del y and apple \n")
for r in X.get_instances():
    print(r.name, end=', ')