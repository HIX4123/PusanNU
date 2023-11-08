#-------------------------------------------------------------------------------
# Purpose:     2020 컴퓨터및 프로그래밍 입문
# Author:      Cho
# Created:     2020-06-08
#-------------------------------------------------------------------------------


def good( **kargs ) :
    for key, values in kargs.items() :
        print(f' key={key}, value={values}')


def foo(a,b,c):
    if a**2 + b**2 == c**2 :
        return( True )
    else :
        return( False )

good(summer=10)
good(tomato=10, banana="맛있다", msg="이건 뭐여?")