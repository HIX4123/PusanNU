
from timeit import Timer



def list_sum():
    mlist=[3,2,1,4,7,9,5,8,6,10,11,12,14,13,15,19,20,18,16,17,\
               875,345,123,32,45,98,5432,4353,65,99]
    sum( mlist )


def tuple_sum():
    mtuple=(3,2,1,4,7,9,5,8,6,10,11,12,14,13,15,19,20,18,16,17,\
                875,345,123,32,45,98,5432,4353,65,99)
    sum( mtuple )

#
# 지정한 함수를 100만번(defaul) 수행한 시간을 돌려주낟ㅈ.
#

tlist = Timer( list_sum )  # 함수 이름을 parameter로 넘겨 줌,
print( f"sum(list) time : {tlist.timeit():10.7}")


ttuple = Timer( tuple_sum )
print( f"sum(tuple)time : {ttuple.timeit():10.7}")