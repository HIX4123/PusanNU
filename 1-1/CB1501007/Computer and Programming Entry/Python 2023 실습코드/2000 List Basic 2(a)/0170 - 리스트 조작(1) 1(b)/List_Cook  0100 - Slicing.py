
print("이것  __name__은 무엇 ?", __name__)

# 실험 1 - 만들고 내부 값 찾아오기
x=["first", "second", "third", "fourh", "fifth", "sixth", "last"]
y=["Jan.", "Feb.", "March", "April", "May", "June", "July", "August", "Sep."]

print("Out 1", x[0], x[1], x[-1])
print("Out 2", y[0:3])
print("Out 3", y[-1], y[-3:-1])

# 실험 2 - 슬라이싱
L = list(range(10))
print(L[1:3])  #기본 슬라이싱
print(L[::2])  #확장 슬라이싱

# 실험 3 - List 고치기 -  정한 위치에 삽입
x[0] = 5123 #내용을 언제든지 바꿀 수 있다.
print(x)
x.append("end")
print("하나 늘인 뒤의 결과",  x)
y.insert(1, -999)
print(" 중간에 하나 삽입 후1 ",  y)
y.insert(0, "Is This?")
print(" 중간에 하나 삽입 후2 ",  y)

