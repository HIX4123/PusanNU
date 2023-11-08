

# 특정 문자로 시작하는 또는 끝나는 문자열인지의 여부를 계산

str = "this is string example....wow!!!";
print ("test0", str.startswith( 'this' ))
print ("test1", str.startswith( 'is', 2, 4 ))
print ("test1.1", str.startswith( 'string', 3, 4 ))
print ("test2", str.startswith( 'this', 2, 4 ))


url='http://www.google.com'

val=url.startswith('http://')
print("test3", "val=", val)


suffix = "wow!!!";
print("test4", str.endswith(suffix))
print("test5",str.endswith(suffix,20))

suffix = "is";
print("test6",str.endswith(suffix,20))
print("test7",str.endswith(suffix, 2, 4))
print("test8",str.endswith(suffix, 2, 6))