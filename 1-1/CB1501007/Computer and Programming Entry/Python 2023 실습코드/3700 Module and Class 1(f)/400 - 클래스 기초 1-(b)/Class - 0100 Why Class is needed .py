# 여러 사람이 공동작업
# 현대 프로그래밍의 기본형식 - 공동작업
# import class


class Person:    # name made in constructor
    def __init__(self, John, age):
        self.name = John
        self.age  = age

    def get_person_name(self):
        return self.name

    def bus_ticket( self):
        if self.age < 65 : return 1200
        else : return 0


A = Person("팽길탄", 26)
W = Person("김노인", 66)

B = A.get_person_name( )

print("B= ", B)
print( W.get_person_name( ), "버스비= ",  W.bus_ticket())
print( A.get_person_name( ), "버스비= ",  A.bus_ticket())

