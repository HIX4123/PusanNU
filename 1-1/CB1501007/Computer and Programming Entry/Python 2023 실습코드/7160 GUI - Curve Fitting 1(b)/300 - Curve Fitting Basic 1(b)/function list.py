
def a( x):
    return x*2

def b( x):
    return x*3

def c( x):
    return x*5

flist= [ a, b, c]    # 함수 뒤에 선언
la = [ 4, 11, 6, 7, 8]

for w in la :
    X =  flist[w%3]
    print(w, X, end=' ')
    print("f(x)=", X( w ))