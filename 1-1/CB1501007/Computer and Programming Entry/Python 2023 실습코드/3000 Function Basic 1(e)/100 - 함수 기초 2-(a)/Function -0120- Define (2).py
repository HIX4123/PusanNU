#
# 함수 정의 및 사용 방법
# 좋은 프로그램, 간결한 프로그램을 작성하기 위해서는 반드시 함수를 사용

def merong(  ):
    pass     # 아무런 동작없이 그대로 돌아가는 , 가장 단순한 함수



def listsum( this, start, end ) :
    s = 0
    for x in range( start, end ) :
          s += this[x]
    return(s)

#-------------- end of function definition -----------

a = 2345
b = 567

def posi_sum( L ) :
    mysum = 0
    for w in L :
        if w > 0 : mysum += w

    return(mysum)



mylist = [1,-2,3,-4,5,-6,7,-8,9]

# format string을 이용해서 출력해보자.
print("리스트 list[0,2] 합은 %d" % listsum( mylist, 0,2))
print("리스트 list[2,4] 합은 %d" % listsum( mylist, 2,6))
print("리스트 list의 전체 합은 %d" % listsum( mylist, 0, len(mylist)))
print("메롱을 불러 봅니다", merong())




