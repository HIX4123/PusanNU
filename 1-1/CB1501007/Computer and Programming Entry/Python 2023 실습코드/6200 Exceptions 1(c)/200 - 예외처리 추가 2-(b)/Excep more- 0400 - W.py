

#define list
numlist = [ 1, 2, 3, 4, 5, 10, 15 ]

print("numlist =", numlist)

print()

# list pop Exception
count = 0
try :
    for i in range(0, 10) : # range 범위까지 numlist pop함수 호출
        print("Pop :", numlist.pop())
        count += 1
except IndexError :
    print("비어있는 리스트에서 pop함수를 수행할 수 없습니다.")
except Exception as e:
    print(type(e))
    print("알 수 없는 에러가 발생하였습니다.")
finally :
    print("리스트의 크기는 ", count, "입니다.")

print()

# list boundary exception
numlist2 = [ 8, 5, 7, 6, 5, 4, 3, 2, 8 ]

try :
    for i in range(0, 50) :         # range 범위 까지 i를 증가시키며 리스트 값을 확인
        print("numlist2[", i, "] =", numlist2[i])
except IndexError :
    print("리스트 인덱스 범위를 벗어나는 값입니다.")

print()

# list 연산 exception (정수 덧셈)
try :
    print(numlist2)

    numlist2 += 3.0     # 리스트에 일반 실수를 더하는 연산 수행
    #numlist2 -= 3

    print(numlist2)

    # 예외가 발생할 경우 이후 작업이 수행되지 않음
    numlist2 *= 2       # 리스트에 정수를 곱함
    print(numlist2)
except TypeError as e:
    print(type(e), "리스트에 적합한 연산이 아닙니다.")