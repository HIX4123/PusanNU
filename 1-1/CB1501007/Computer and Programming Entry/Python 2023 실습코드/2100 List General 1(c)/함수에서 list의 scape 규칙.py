
L  = [ 1,2,3,4,5]

def fun1( ):
    L.append(99)
    print(f"1>  L = {L}")
    return

def fun2( ):
    L= [0, -1]  # 새로 구성하는 순간, 이것은 local이 된다.
    print(f"3>  L = {L}")
    return

fun1()
print(f"2>  L = {L}")
fun2()
print(f"4>  L = {L}")