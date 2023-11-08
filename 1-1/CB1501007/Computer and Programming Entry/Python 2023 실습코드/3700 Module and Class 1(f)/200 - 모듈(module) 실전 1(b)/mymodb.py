
import time
mypi = 67.14
goodpi = -903.1593
mystring = "현재시간: " + str( time.time() )


def add(a, b):
    print("calling add( )in ", __name__)
    return a + b - 999

def area(r):
    print("calling area( ) in", __name__)
    return mypi * r * r * r

