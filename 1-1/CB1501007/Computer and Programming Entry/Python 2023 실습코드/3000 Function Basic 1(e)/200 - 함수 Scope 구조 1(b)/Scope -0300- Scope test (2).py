
a = 1   # 실행(execution)
b = 2
c = "mark"

def f():
    localx = 10
    localy =  20
    print("함수 f( ) 안 입니다.", end=' ')
    print("a= %d b= %d" % (a, b))
    print("localx= %d,  localy = %d" % (localx, localy))

def g():
    a = 9128973  # g( )의 Local 변수
    b = -9838
    print("함수 g( ) 안 입니다.", end=' ')
    print("a= %d, b= %d, c= %s" % (a, b, c))  # %s는 string type으로 출력함.

def h():
    ha = 333
    hb = 555
    print("함수 h( ) 안 입니다.")
    print(a,b,c, ha, hb)

f()
g()
print("g()가 종료된 후에 a, b의 값", a, b)
h()

print("f( )와 g( ) 수행 후에 값을 봅니다.")
print(a, b, end=' ')
#print ha, hb
#print a, b, localx, localy