
# 함수형 언어에서 제공 함수, 이름없는 함수

add = lambda x,y : x + y

def myadd(x,y):
    s = x + y
    return( s )

print( add(10,20))

w = (lambda x,y: abs(x-y))(100,88)

print("w=", w)