
# class13.py

class MyDict:
        def __init__(self, d=None):
                if d == None: d = {}
                self.d = d
        def __getitem__(self, k): # key
                return self.d[k]
        def __setitem__(self, k, v):
                self.d[k] = v
        def __len__(self):
                return len(self.d)

m = MyDict()

m['day']= 'light'
m['night'] = 'darkness'
print(m)
print(m['day'])            #
print(m['night'])          # __getitem__ ?몄텧
print(len(m))              # __len__ ?몄텧
