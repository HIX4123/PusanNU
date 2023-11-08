

import collections

class MyString(collections.MutableString):
    def __init__(self, data):
        collections.UserString.__init__(self, data)


s = MyString('python rules!')
s[0] = 'P'
print(s)
s[:6] = 'PYTHON'
print(s)
