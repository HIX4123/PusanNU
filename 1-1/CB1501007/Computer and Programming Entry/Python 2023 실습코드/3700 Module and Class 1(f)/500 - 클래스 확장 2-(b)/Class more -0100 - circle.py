
import importlib
#from . import importlib  # importlib을 생략할 수 있다. 약간 위험
import circle

#reload(circle)
importlib.reload(circle)  # 이것을 사용하면 byte code  *.pyc 가 만들어진다.

kong = circle.Circle(5,5,10)

points= [ (13,2), (5,8), (9,0), (7, 8) ]
print( "area=", kong.area())

for w in points :
    x= w[0]
    y= w[1]
    print( f'inout({x:2},{y:2}) = {kong.inout(x,y)}')

print( "center=", kong.center())
