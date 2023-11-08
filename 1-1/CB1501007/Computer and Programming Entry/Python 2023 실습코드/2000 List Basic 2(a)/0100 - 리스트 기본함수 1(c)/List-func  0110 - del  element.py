# 리스트(List) 처리하기

numbers = list(range(10))
print( numbers )
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# 삭제
del numbers[:3] # 0, 1, 2를 삭제 함.
print( numbers )

a=input("뭐라도 치보라고:")
print(f"당신의 입력은 {a}")

# 수정
numbers[1:3] = [66, 77]
print( numbers )

numbers[1:5] = [0, 0]  #1부터 4까지 메꿔 넣음
print( numbers )

print("끝이랑께")
