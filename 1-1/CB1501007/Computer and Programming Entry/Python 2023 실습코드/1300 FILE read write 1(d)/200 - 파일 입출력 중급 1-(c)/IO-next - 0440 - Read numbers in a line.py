
print("숫자 읽기 다른 버전:")
numbers = [int(n) for n in input("숫자를 공백으로 분리하여 입력:").split()]

print(("입력된 수는=", numbers))
print(("그 합은 = ", sum(numbers)))