
# Exception 기본 문법
#
#   try:
#       You do your operations here;
#       ......................
#   except ExceptionI:
#       If there is ExceptionI, then execute this block.
#   except ExceptionII:
#       If there is ExceptionII, then execute this block.
#       ......................
#   else:
#       If there is no exception then execute this block.
#
import sys


# 기본적인 연산 오류 발생 (ZeroDivisionError)
n = [ 4, 6, 7, 8, 9 ]
m = [ 7, 4, 9, 8, 10 ]

for i in range(0,5) :
    numerator = n[i] + m[i]
    denominator = abs(n[i] - m[i] ) # 예외 처리를 하지 않을 경우 오류 메시지 발생

    print("Result : ", numerator / denominator)


# 정의되지 않는 변수 사용 (NameError)
#spam = 4

for i in range(0,5) :
    numerator = spam * n[i]
    print(numerator)


# 연산 중에 각 인수의 타입이 많지 않을 경우 오류 발생 (TypeError)
value1 = '2'
value2 = 4

print(value1 + value2) # 문자와 정수간에 타입 변환 없이 연산을 수행할 경우 에러 발생


# 정상적인 파일 출력이 될 경우
try:
    fh = open("writefile.out", "w")
    fh.write("This is my test file for exception handling!!")
except IOError:
    print("Error: can\'t find file or read data")
else:
    print("성공적으로 파일이 출력되었습니다.")
    fh.close()

print()

# .py를 수행하는 폴더 내부에 읽을 파일이 없을 경우
try:
    fh = open("writefile.inp", "r")
except IOError:
    print("Error: can\'t find file or read data")
else:
    fh.readline();
    print("성공적으로 파일이 읽어졌습니다.")

print()

# 정수를 0으로 나누었을 때 예외가 발생하는 경우
numlist = [ 4, 6, 7, 8, 0, 9, 11]

try :
    for i in numlist :
        k = 1.0 / i
        print("Inverse Result : ", i)
except ZeroDivisionError as msg :
    print('Run-time error: ', msg)
else :
    print(x)

print()

