

from collections import UserList

class myList(UserList): # UserList
    def __init__(self, d=None):
        UserList.__init__(self, d)
    def push(self, d):
        self.data.append(d)

ls = myList([1,2,3])    # ?몄뒪?댁뒪 ?앹꽦
ls.push(4)              # push
ls.push(5)
print(ls.pop())          # 5
print(ls.pop())          # 4
print(ls)                        # [1, 2, 3]
