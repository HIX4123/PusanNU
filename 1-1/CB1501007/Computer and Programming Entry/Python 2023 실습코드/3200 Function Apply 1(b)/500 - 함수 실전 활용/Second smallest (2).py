# 리스트에서 하나씩 token type으로 읽는 연습을 합니다.


def find_second_smallest(L):  # 함수를 만들어
    smallest = min(L)
    print(smallest)
    min1 = L.index(smallest)
    L.remove(smallest)
    next_smallest = min(L)
    min2 = L.index(next_smallest)
    return min2
# ------- end of 함수 find_second_smallest ---------

def get_positive( L ) :     # 리스트에서 양수만 골라 담은 리스트를 만들어 준다.
    newl= [ ]
    retun ( newl )


def rotate( L,k ) :           # 리스트의 원소를 왼쪽으로 k칸 돌려준다.
    return( L )

mylist = [ 54, 65, 11, 32, 6, 7, 10, 98 ]

print("처리 전 L1 =", mylist)
x=find_second_smallest( mylist )
print("smallest index = ", x)
print("처리 후 L1 =", mylist)


youlist = [ 8, -90, 45, 21, -32, 55, -7, -23, 78, 6, -3]


