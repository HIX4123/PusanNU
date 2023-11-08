# Problem Solving Class A
# 파일에 한 줄에 여러 개의 자료(token)이 있을 때
# 하나씩 token type으로 읽는 연습을 합니다.

numbers = list( input('숫자를 여러개 입력하시오: ').split())
ln= list(map(int, numbers))
# numbers의 각 원소에 int 함수를 적용한 다음에 list로 만듬

print("number=", numbers)
print("min number=", min(numbers))
print("max number=", max(numbers))

print(ln)
print( sum(ln) )