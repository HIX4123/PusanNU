
# str.is.. 하면 안됨. str( )은 function으로 인식
#



print("헤이")
mstr = "this2009";  # No space in this mstring
print("exp 1= ", mstr.isalnum())

mstr = "this is mstring example....wow!!!";
print("exp 2= ", mstr.isalnum())

mstr = "this";  # No space & digit in this mstring
print("exp 3= ", mstr.isalpha())

mstr = "this is mstring example....wow!!!";
print("exp 4= ", mstr.isalpha())

mstr = "123456";  # Only digit in this mstring
print("exp 5= ", mstr.isdigit())

mstr = "this is mstring example....wow!!!";
print("exp 6= ", mstr.isdigit())

mstr = "this2009";
print("exp 7= ", mstr.isnumeric())

mstr = "23443434";
print("exp 8= ", mstr.isnumeric())