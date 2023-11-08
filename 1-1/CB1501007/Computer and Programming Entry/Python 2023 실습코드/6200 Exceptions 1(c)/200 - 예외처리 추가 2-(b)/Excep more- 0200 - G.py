

# multiple Exception
try:
    f = open('myfile.txt')
    s = f.readline()
    i = int(s.strip())  # 파일 내부에 있는 문자열을 정수로 변환
except IOError as e:
    print("I/O error({0}): {1}".format(e.errno, e.strerror))
except ValueError:
    print("Could not convert data to an integer.")   # 문자열이
except:
    print("Unexpected error:", sys.exc_info()[0])
    raise

print()

#raise를 이용한 Exception Handling
try:
    n = [ 4, 6, 7, 8, 9 ]
    m = [ 7, 4, 9, 8, 10 ]

    for i in range(0,5) :
        numerator = n[i] + m[i]         # 두개의 리스트에서 같은 번지의 내용을 더한 값을 저장
        denominator = abs(n[i] - m[i] ) # 두개의 리스트에서 같은 번지의 내용을 뺀 값을 저장

        if denominator == 0 :           # 분모가 0이면 예외 발생
            raise Exception

        print("Result : ", numerator / denominator)
except Exception:
   print("분모가 0이 아닌 숫자가 와야 합니다.")
else:
   print("Result : ", a/b)

print()

# try - except - finally 문법 사용
f = open('exceptio.out', 'w')

try :
    n = [ 4, 6, 7, 8, 9 ]
    m = [ 7, 4, 9, 8, 10 ]

    for i in range(0,5) :
        numerator = n[i] + m[i]         # 두개의 리스트에서 같은 번지의 내용을 더한 값을 저장
        denominator = abs(n[i] - m[i] ) # 두개의 리스트에서 같은 번지의 내용을 뺀 값을 저장

        print("Result : ", numerator / denominator, file=f)
except ZeroDivisionError as msg :
    print('Run-time error : ', msg)
finally :
    print('file close')
    f.close()

print()

# 입력 값을 정수로 변환하는 함수
def valueConvert(var):
   try:
      return int(var)
   except ValueError as Argument:
      print("정수로 변경할 수 없는 값이 입력되었습니다.\n", Argument)

# 정수가 아닌 값을 이용하여 valueConvert 함수 호출
valueConvert("xyz");

