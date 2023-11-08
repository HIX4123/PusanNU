
la = sorted([3, 1, 9.5,  2])    # list
lb = sorted(['a', 'c', 'b'])    # 문자열 리스트
lc = sorted("zeroCola")         #문자열도 가능하다.
ld = sorted((-5.67, True, 3, 2, 1, 56.7))   # Tuple도 가능

print("la= ", la)
print("lb= ", lb)
print("lc= ", lc)
print("ld= ", ld)

# 리스트 자료형에도 sort라는 함수가 있다.
# 하지만 리스트 자료형의 sort 함수는 리스트 객체
# 그 자체를 정렬만 할 뿐 정렬된 결과를 리턴하지는 않는다.
# 다음 예제로 sorted 함수와 리스트 자료형의 sort 함수의 차이점을 확인해 보자.

a = [3, 1, 2, 9, 0, 4, 7]
result = a.sort()
print(result)
print("a.sort() => ", a)

lst=[ 4, 5, 6, 8, 7, 9]
if sorted(lst) == lst:
    print("예, 정렬이 되었습니다.")
else :
    print("아니오. 정렬이 되지 않았습니다. ")
    # code here
