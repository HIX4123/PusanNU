#-------------------------------------------------------------------------------
# Purpose:     2020 컴퓨터및 프로그래밍 입문
# Author:      Cho
# Created:     2020-05-04
#-------------------------------------------------------------------------------

# fast proto-typing lang.
# A.I.   X-algorithm C 3달 작성.... x
#                       2주 ---> C, C++


# 망원경의 법칙
#  7인치 망원경을 하나 만드는 시간보다
#  3인치, 7인치 망원경을 만드는 시간이 짧다.


# defensive programming...


la=[100,43,33,25,23,-90]

def shrink(L) :
    if len(L) >= 100:  print("error: 학생 수가 이상함")
    if len(L) <= 2 :
        print("error: shrink()" ) # coder 생성한 메시지
        return
    L.pop()
    L.pop(0)


