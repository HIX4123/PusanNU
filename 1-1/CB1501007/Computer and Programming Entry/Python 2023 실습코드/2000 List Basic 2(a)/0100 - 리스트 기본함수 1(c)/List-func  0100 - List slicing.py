# 리스트(List) 처리하기

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



