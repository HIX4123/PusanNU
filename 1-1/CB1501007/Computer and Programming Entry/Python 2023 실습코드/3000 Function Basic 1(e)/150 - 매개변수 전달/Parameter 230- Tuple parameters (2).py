
# 매개변수가 반드시 하나 이상 들어올 때
# 처음 매개변수는 num1, 나머지는 튜플에 저장


def Func(num1, *nums):
    print(num1, nums)

Func(1, 2, 3, 4, 5, 6, 100 )

Func(1, 5, 6, 7) # tuple

