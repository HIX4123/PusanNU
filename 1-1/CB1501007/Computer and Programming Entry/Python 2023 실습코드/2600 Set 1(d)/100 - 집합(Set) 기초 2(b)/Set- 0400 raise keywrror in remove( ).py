#-------------------------------------------------------------------------------
# Purpose:     2020 Prof. Zoh's Work
# Author:      Cho
# Created:     2020-06-24
#-------------------------------------------------------------------------------


s1 = set('catsummertime')

for w in list("crazymanger") :
    try :
        s1.remove( w ) # 에러가 발생할 가능성이 있는 코드
    except KeyError :  # 에러 종류
        print(f' 없는 원소 [{w}]를 set에서 remove( )할 때의 오류')
        #에러가 발생 했을 경우 처리할 코드