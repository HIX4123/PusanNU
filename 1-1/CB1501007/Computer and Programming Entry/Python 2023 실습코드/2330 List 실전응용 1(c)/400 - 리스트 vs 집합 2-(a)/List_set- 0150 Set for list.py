
import string  # 문자열에 대한 특별한 처리를 위해서 import 함

print("실험 1. 집합")

dog = 345
cat = 345
pig = 299
seta = { 1, 1, 1, "star", "craft", "what", "Book", dog , 0.1 }
setb = { pig, cat, 1, 2, 2, "STAR", "craft", "did", dog, 1.0/10 }
print("집합 a를 출력합니다", seta)
print("집합 b를 출력합니다", setb)

seta.add("NEW") # 값 하나 추가 : add(x)
print("결과 2",seta)

setc = set([1,2,3])

setc.update([5,6,7,8,9,10]) # 값 여러개 추가 : update(x)
print("결과 3", setc)

# 값 제거 : remove(x)
setc.remove(10)
print("결과 4", setc)

# 집합 set1 제거
del setc


# 질문. set type에 사용할 수 있는 method( )를 모두 찾아 봅시다.