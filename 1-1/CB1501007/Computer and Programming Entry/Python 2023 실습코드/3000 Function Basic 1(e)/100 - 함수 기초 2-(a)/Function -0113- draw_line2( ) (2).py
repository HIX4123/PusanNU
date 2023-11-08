#-------------------------------------------------------------------------------
# Purpose:     2020 컴퓨터및 프로그래밍 입문
# Author:      Cho
# Created:     2020-04-14
#-------------------------------------------------------------------------------

L="Are you Going to Scarborugh Fair Parsely Sage and Rosemary and Thmye".split()

def mystar( k, c ) :  # k를 파라매터
    # body
    print(k*c)



for i,w in enumerate(L) :
    if i%3 == 0 : mystar(20, "=")
    print(w)


mystar(40,"@")
