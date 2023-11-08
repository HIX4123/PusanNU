


a = [ "cool", "time", "2016", "summer", "radiohead" ]

a.insert(0, "chicken") # 맨 앞에 새 요소 추가
print(a)

a.append("ZZZ") # 맨 뒤에 새 요소 추가
print("실험 1: ", a)

a.pop(0) # 맨 앞의 요소 제거
print("실험 2: ",a)

s = a.pop() # 맨 마지막 요소 제거
print("실험 3: ",a)

a[1:3]=[] # 중간 특정 구간의 원소를 지운다.
print("실험 4:",a)

print("실험 5:", "-----".join(a))

# del a[x]는 x번째 요소값을 삭제한다.
# del 함수는 # 파이썬이 자체적으로 가지고 있는 내장 함수. 일반형.
# 사용형식 : del 객체
# 참고 - 객체란 파이썬에서 사용되는 모든 자료형을 말한다.)

del a[-1]
print("실험 6:",a)
