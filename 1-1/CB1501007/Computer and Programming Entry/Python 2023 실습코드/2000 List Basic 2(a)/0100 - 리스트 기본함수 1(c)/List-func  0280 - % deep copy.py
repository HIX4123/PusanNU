
# Purpose: deep copy:
# List에서 Copy를 할 때는 매우 유의해야 한다.

import copy  # deep copy를 하기 위해서는 반드시 필요하다,

setmenu = [' hamburger', 'coffee']
la = [ 'ipad', 'galaxy', 'usb' ]
lb = la

print("id(la) = %d, id(lb)= %d" % (id(la), id(lb)))
print("a is b 인가요 %s " % (la is lb ))

la.append('notebook')
la.append( setmenu)
print("la = ", la)
print("lb = ", lb)


myla = copy.copy( la )
yourla = copy.deepcopy( la )
la.pop(0)

print("la after pop()     = " , la)
print("myla after pop()   = ", myla)
print("yourla after pop() = ", yourla)

# 자 지금부터 deepcopy와 일반 copy의 차이점을 봅니다.

setmenu.pop(0)
print("\n\nsetmenu.pop(0) = ", setmenu)
print("la after setmenu     = " , la)
print("myla setmenu   = ", myla)
print("yourla setmenu = ", yourla)
# 차이가 이해가 됩니까 ? ㅎㅎㅎ