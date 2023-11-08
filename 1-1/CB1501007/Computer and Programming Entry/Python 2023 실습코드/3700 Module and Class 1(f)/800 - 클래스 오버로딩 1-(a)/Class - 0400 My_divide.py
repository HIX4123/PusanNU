
# Operator 오버로딩 (중첩)

class MyString:
    def __init__(self, str):
        self.str = str
    def __truediv__(self, sep):     # Overloading operator
            return self.str.split(sep)      #

m = MyString("abcdabcdabcd")
print( m / "b" )       # 내가 정한 나눗셈을 객체 클래스에 적용.
print( m / "bc")      #


Q = MyString("나는 바보야")

print ( Q / "바" )