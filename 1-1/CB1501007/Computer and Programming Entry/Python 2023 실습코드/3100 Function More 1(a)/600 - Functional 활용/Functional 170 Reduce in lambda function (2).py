
"""
 reduce는 반복 가능한 객체의 각 요소를 지정된 함수로 처리한 뒤 이전 결과와
 누적해서 반환하는 함수입니다(reduce는 파이썬 3부터 내장 함수가 아닙니다.
 따라서 functools 모듈에서 reduce 함수를 가져와야 합니다)

 from functools import reduce
 reduce(함수, 반복가능한객체)

다음은 리스트에 저장된 요소를 순서대로 더한 뒤 누적된 결과를 반환합니다.
"""
from functools import reduce

def f(x, y):
    return x + y

a = [1, 2, 3, 4, 5]

rsum = reduce(f, a)
print("rsum1= ", rsum)

rsum = reduce(lambda x, y: x * y, a)
print("rsum2= ", rsum)



