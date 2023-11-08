
import time
mypi = 3.14
goodpi = 3.141593
mystring = "현재시간: " + str( time.ctime() )

def add(a, b):
    ''' 두 수를 더하는 함수 '''
    print("calling add( ) in", __name__)
    return a + b

def area(r):
    ''' 주어진 반지름에 해당하는 원을 넓이 구하기'''
    print("calling area( ) in", __name__)
    return mypi * r * r



print("여기는 mymoda.py", mystring)
