
# 함수 정의 및 인수 전달 (parameter passing)

def dog( food ):
    food = "개밥"

def cat( food ) :
    print("in cat( )")
    print("고양이 밥은 = ", food)
    food = "생선"

def snake( foods ):
    print(foods[0]) # 리스틔 경우 내부 원소의 변화는 반영된다.
    foods[0] = "쥐"



x = "누룽지"
y = [ "병아리", "벌레", "개미", "지렁이"]

dog(x)
cat(x)

# print food
print(x)

print("Before snake( ) call", y[0])
snake(y)
print("After snake( ) call", y[0])