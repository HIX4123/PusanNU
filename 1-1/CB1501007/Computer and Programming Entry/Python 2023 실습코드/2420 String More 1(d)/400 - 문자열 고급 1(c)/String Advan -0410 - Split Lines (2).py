
# The method splitlines() returns a list with all the lines in string,
# optionally including the line breaks (if num is supplied and is true)

# str.splitlines( num=string.count('\n'))

str = "Line1-a b c \n\nd e f\nLine2- a b c\n\nLine4- a b c d";
print(str.splitlines( ))
print(str.splitlines( 0 ))
print(str.splitlines( 1 ))
print(str.splitlines( 2 ))
print(str.splitlines( 3 ))
print(str.splitlines( 4 ))
print(str.splitlines( 5 ))