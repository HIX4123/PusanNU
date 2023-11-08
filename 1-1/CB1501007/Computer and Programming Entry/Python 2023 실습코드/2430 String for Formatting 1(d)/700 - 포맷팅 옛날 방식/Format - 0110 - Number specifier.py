
#d Signed integer decimal.
#i Signed integer decimal.
#o Unsigned octal. (1)
#u Unsigned decimal.
#x Unsigned hexadecimal (lowercase). (2)
#X Unsigned hexadecimal (uppercase). (2)
#e Floating point exponential format (lowercase). (3)
#E Floating point exponential format (uppercase). (3)
#f Floating point decimal format. (3)
#F Floating point decimal format. (3)
#g Floating point format. Uses exponential format if exponent is greater than -4 or less than precision, decimal format otherwise. (4)
#G Floating point format. Uses exponential format if exponent is greater than -4 or less than precision, decimal format otherwise. (4)
#c Single character (accepts integer or single character string).
#r String (converts any python object using repr()). (5)
#s String (converts any python object using str()). (6)

a=1067
b= -100
c= 67
d= 1024
e= 3.1415
f= 1.5345e10
g='W'  #specifier , 지시자

numlist= [ 345, 23, -867,  89345, -94384, 5, 67 ]

print("a=%d b=%d c=%d d=%d e=%e" % (a, b, c, d, e))
print("a=%10d b=%10d c=%10d d=%10d e=%10e" % (a, b, c, d, e))
print("a=%d b=%d c=%d d=%d e=%e" % (a, b, c, d, e))

print("a=%09i " % a)

print("\n %d 형식을 사용함")
for x in numlist :
    print("x = %d" % x)

print("\n %10d 형식을 사용함")
for x in numlist :
    print("y = %10d" % x)

print("\n %-10d 형식을 사용함")
for x in numlist :
    print("z = %-10d" % x)

print("\n +-10d 형식을 사용함")
for x in numlist :
    print("z = %+-10d" % x)

m='computer'
print('m[0]=', m[0])

