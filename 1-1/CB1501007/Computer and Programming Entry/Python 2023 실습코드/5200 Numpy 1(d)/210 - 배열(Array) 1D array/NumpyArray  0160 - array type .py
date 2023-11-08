
import array
import binascii

s = 'This is the array.'
a = array.array('c', s)  # 오류

print('As string:', s)
print('As array :', a, type(a))
print('As hex   :', binascii.hexlify(a))
