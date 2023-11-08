#-------------------------------------------------------------------------------
# Author:      Zoh
# Created:     2019-08-29
#-------------------------------------------------------------------------------

print("\n Padding zeros into a number")
for i in (1, 10, 100, 837, 45, 345831):
    print( f'num = {i:010}')  #앞에 0으로 시작하면 0을 패딩


print("\n\n Padding zeros into a number by >010")
for i in (1, 10, 100, 837, 45, 345831):
    print( f'num = {i:>010}')  #앞에 0으로 시작하면 0을 패딩




print("\n Padding zeros into a hexa string")
for w in (1, 10, 100, 837, 45, 345838231):
    s = hex(w)
    print(f'num = {s:>015}')