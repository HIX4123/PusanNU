# input( )으로 여러 숫자를 읽어들이기


numbers = [int(n) for n in input("숫자를 공백으로 분리하여 입력:").split()]

print(("입력된 수의 리스트(list)=", numbers))
print(("그 합은 = ", sum(numbers)))