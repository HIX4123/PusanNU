
la= [ -33, 45, 0, 66, 12, 99, 40 -89]

def rotate_right(L):
    this = L.pop()
    L.insert(0, this )


def rotate_left(L):
    a = L.pop(0)
    L.append(a)
#----- 왼쪽으로 하나 회전하는 함수 -----------


def rotate_more(k, L) :
    for i in range( k ) :
        rotate_left(L)


print("Before=", la)
rotate_more(4, la )
print("After=", la)


