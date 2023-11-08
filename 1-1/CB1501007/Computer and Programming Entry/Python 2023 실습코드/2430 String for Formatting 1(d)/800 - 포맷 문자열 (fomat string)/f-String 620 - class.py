#-------------------------------------------------------------------------------
# Author:      Zoh
# Created:     2020-04-12
#-------------------------------------------------------------------------------


class User:
    def __init__(self, name, occupation):
        self.name = name
        self.occupation = occupation

    def __repr__(self):
        return f"[{self.name}] 은/는 {self.occupation} 입니다."

lu = [ User('공달수', '날백수')   ,    User('사동팔', '양아치') , \
      User('조환규', '교수남')   ,     User('Bread', '빵')  ]

for w in lu :
    print(f'{w}')