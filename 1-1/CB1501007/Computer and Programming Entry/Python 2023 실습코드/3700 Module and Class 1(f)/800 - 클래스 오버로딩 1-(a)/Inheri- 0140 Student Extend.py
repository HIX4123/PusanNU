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
        print ("학생 한 명을 생성했습니다.")

    def PNUyear(self, thisyear) :
        m = thisyear - self.year + 1
        if m >= 4 : self.studyear = 4
        else : self.studyear = m
        print ("학생의 학년은 ===>", self.studyear)

    def PNUprint(self) :
        print ("\n --------P N U ------------ ")
        print ("학생의 이름=", self.name)
        print ("학생의 학과=", self.dept)
        print ("학생의 입학년도= ", self.year)
        if self.studyear == 0 : print ("학년을 확인할 수 없습니다. ")
        else : print ("부산대학교의 [ ", self.studyear, "] 학년 입니다.")
# --------------- end fo class PNUstuednt (내국인) -------------------


class PNUall( PNUstudent) :
    def __init__(self, name, dept, year, country) :
        PNUstudent.__init__(self, name, dept, year)
        self.country = country

    def PNUprint(self) :
        PNUstudent.PNUprint(self)
        print ("학생의 국적은 = ", self.country, "입니다")

# ------------ end of class PNUall ----------------------

A = PNUstudent("Sora", "CS", 2007)
A.PNUyear(2012)
B = PNUall    ("dalsik", "math", 2012, "US")
A.PNUprint()
B.PNUprint()



