
import string  # 문자열에 대한 특별한 처리를 위해서 import 함

print("실험 1. 집합")

dog = 345
cat = 345
pig = 299
seta = { 1, 1, 1, "star", "craft", "what", "Book", dog , 0.1 }
setb = { pig, cat, 1, 2, 2, "STAR", "craft", "did", dog, 1.0/10 }
print("집합 a를 출력합니다", seta)
print("집합 b를 출력합니다", setb)


# 집합 선언
set1 = set([1,2,3])
set2 = set([2,4,5,6])
set3 = set() # 공집합

# set1과 set2의 교집합
print("Set AND1", seta & setb)
print("Set AND2", seta.intersection(setb))

# set1과 set2의 합집합
print("Set OR1", seta | setb)
print("Set OR2", seta.union(seta))

# set1과 set2의 차집합
print("Set Difference1", seta - setb)
print("Set Difference2", seta.difference(setb))
print("Set Difference3", setb.difference(seta))

# set1과 set2의 합집합에서 교집합을 뺀 차집합
print("Set Exclusive OR", seta ^ setb)
