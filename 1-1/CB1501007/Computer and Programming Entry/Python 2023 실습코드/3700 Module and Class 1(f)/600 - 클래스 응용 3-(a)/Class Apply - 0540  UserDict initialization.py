

import UserDict

class MyDict(UserDict.UserDict):
    def __init__(self, data={}, **kw):
        UserDict.UserDict.__init__(self)  #
        self.update(data)       #
        self.update(kw) #
    def keys(self):
        ks = list(self.data.keys())
        ks.sort()
        return ks

a = MyDict(a=1, b=2, c=3, d=4)
print(a)
print(list(a.keys()))
