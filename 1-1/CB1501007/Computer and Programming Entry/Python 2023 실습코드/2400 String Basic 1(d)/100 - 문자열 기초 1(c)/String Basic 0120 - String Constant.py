# https://docs.python.org/3/library/string.html


import string

print("Out 2 ==>", string.ascii_letters)
print("Out 3 ==>", string.ascii_lowercase)
print("Out 4 ==>", string.ascii_uppercase)
print("Out 5 ==>", string.digits)
print("Out 6 ==>", string.hexdigits)
print("Out 7 ==>", string.ascii_letters)
print("Out 8 ==>", string.punctuation)
print("\n printable ==>", list(string.printable))
print("\n whitespace ==>", list(string.whitespace))

x = '8'
if x in string.ascii_letters :
    print("x는 문자입니다")
else :
    print("x=", x, "는 문자가 아닙니다.")


print( "type=",  type( string.ascii_lowercase) )

