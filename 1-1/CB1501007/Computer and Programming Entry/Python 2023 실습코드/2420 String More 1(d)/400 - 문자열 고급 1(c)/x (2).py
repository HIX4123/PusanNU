

print("헤이")
str = "this2009";  # No space in this string
print("exp 1= ", str.isalnum())

str = "this is string example....wow!!!";
print("exp 2= ", str.isalnum())

str = "this";  # No space & digit in this string
print("exp 3= ", str.isalpha())

str = "this is string example....wow!!!";
print("exp 4= ", str.isalpha())

str = "123456";  # Only digit in this string
print("exp 5= ", str.isdigit())

str = "this is string example....wow!!!";
print("exp 6= ", str.isdigit())

str = "this2009";
print("exp 7= ", str.isnumeric())

str = "23443434";
print("exp 8= ", str.isnumeric())