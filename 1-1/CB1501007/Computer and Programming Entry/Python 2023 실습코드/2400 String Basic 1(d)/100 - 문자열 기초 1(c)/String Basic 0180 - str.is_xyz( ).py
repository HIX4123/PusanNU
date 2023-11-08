

str = "this2009";  # No space in this string
print("exp 1= ", str.isalnum())

str = "this is string example....wow!!!";
print("exp 2= ", str.isalnum())

str = "this";  # No space & digit in this string
print("exp 3= ", str.isalpha())

str = "this is string example....wow!!!";
print("exp 4= ", str.isalpha())

str = "123456 ";  # Only digit in this string
print("exp 5= ", str.isdigit())  #공백은 digit이 아님

x = '3²'
print("exp 6= ", x, x.isdigit() )

"""
numeric 하다는 것은 보다 넓은 의미인데, isdigit()은 단일 글자가 ‘숫자’ 모양으로 생겼으면 True를 리턴한다고 했다. isnumeric()은 숫자값 표현에 해당하는 텍스트까지 인정해준다.
예를 들어 “½” 이런 특수문자도 isnumeric()에서는 True로 판정된다.
"""

str = "this is string example....wow!!!";
print("isdigit() exp 6= ", str.isdigit())

str = "일이삼사오";
print("exp 7= ", str.isnumeric())

str = "2344.3434";
print("exp 8= ", str.isnumeric())