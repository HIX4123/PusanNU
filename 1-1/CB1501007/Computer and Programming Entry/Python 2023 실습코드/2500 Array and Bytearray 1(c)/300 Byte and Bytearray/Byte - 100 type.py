#-------------------------------------------------------------------------------
# Author:      Zoh
# Created:     2019-08-29
#-------------------------------------------------------------------------------

Bytea = bytes(18)
print("type Bytea =", type( Bytea ) )



Byteb = b'\x01\x21\31\41'
print("type Byteb = ", type( Byteb)   )

testBytes = b'\xF1\x10'
x = int.from_bytes(testBytes , byteorder='big')
print("x=", x )

w=0
x = int.from_bytes( b'\x00' , byteorder='big')
print("zero byte b'0'=", x )


a = b'\xde\xad\xbe\xef'.hex()
print("a= ", a )


b = bytes.fromhex(a)
print("b= ", b)
