#-*- coding: cp949 -*-
# Purpose:

Eng = ["CS", "Mech", "Elec", "Chem", "Arch", "Civil"]
Art = [ "Lang", "Music", "Edu", "Phy" ]

class PNUstudent :

    def __init__ (self, name, dept, year ) :
        self.name = name
        self.dept = dept
        self.year = year
        self.studyear = 0
        print ("�л� �� ���� �����߽��ϴ�.")

    def PNUyear(self, thisyear) :
        m = thisyear - self.year + 1
        if m >= 4 : self.studyear = 4
        else : self.studyear = m
        print ("�л��� �г��� ===>", self.studyear)

    def PNUprint(self) :
        print ("\n --------P N U ------------ ")
        print ("�л��� �̸�=", self.name)
        print ("�л��� �а�=", self.dept)
        print ("�л��� ���г⵵= ", self.year)
        if self.studyear == 0 : print ("�г��� Ȯ���� �� �����ϴ�. ")
        else : print ("�λ���б��� [ ", self.studyear, "] �г� �Դϴ�.")
# --------------- end fo class PNUstuednt (������) -------------------


class PNUall( PNUstudent) :
    def __init__(self, name, dept, year, country) :
        PNUstudent.__init__(self, name, dept, year)
        self.country = country

    def PNUprint(self) :
        PNUstudent.PNUprint(self)
        print ("�л��� ������ = ", self.country, "�Դϴ�")

# ------------ end of class PNUall ----------------------

A = PNUstudent("Sora", "CS", 2007)
A.PNUyear(2012)
B = PNUall    ("dalsik", "math", 2012, "US")
A.PNUprint()
B.PNUprint()



