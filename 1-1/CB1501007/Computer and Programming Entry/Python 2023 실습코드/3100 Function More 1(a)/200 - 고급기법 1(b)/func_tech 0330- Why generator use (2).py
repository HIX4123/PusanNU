
#  위와 같은 generator 함수를 좀 더 쉽게 사용할 수 있도록 generator expression 을 제공한다.
#  list comprehension 과 비슷하지만, [ ] 대신 ( ) 를 사용하면 된다.
#  아래는 0 ~ 9 사이 정수 중 홀수 를 list 와 generator object 로 생성한 예제이다.

import sys

la = [ i for i in range(10) if i % 2 ]
print(la)

lb = ( i for i in range(10) if i % 2 ) # ( )를 사용하면 generator가 된다.
print(lb)

for w in lb:
    print("w=", w)

# list 의 경우 사이즈가 커질 수록 그만큼 메모리 사용량이 늘어나게 된다. 하지만,
# generator 의 경우는 사이즈가 커진다 해도 차지하는 메모리 사이즈는 동일하다.
# 이는 list 와 generator의 동작 방식의 차이에 기인한다.
# list 는 list 안에 속한 모든 데이터를 메모리에 적재하기 때문에 list의
# 크기 만큼 차지하는 메모리 사이즈가 늘어나게 된다. 하지만 generator 의 경우
# 데이터 값을 한꺼번에 메모리에 적재 하는 것이 아니라 next() 메소드를 통해
# 차례로 값에 접근할 때마다 메모리에 적재하는 방식이다.
# 따라서 list 의 규모가 큰 값을 다룰 수록 generator의 효율성은
# 더욱 높아지게 된다.

print(sys.getsizeof( [i for i in range(100) if i % 2] ))    # list
print(sys.getsizeof( [i for i in range(50000) if i % 2] ))
print(sys.getsizeof( (i for i in range(100) if i % 2) ))    # generator
print(sys.getsizeof( (i for i in range(50000) if i % 2) ))

