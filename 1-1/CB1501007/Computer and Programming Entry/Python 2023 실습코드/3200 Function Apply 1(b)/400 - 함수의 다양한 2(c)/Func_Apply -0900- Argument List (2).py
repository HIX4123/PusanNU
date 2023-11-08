# 넘겨줄 변수가 한 개 이상인 경우 제어하는 방법


def maximum(*numbers):
    if len(numbers) == 0:
        return(None)
    else:
        max = numbers[0]
        for n in numbers[1:]:
            if n > max: max = n
        return max


def exampleFun(x, y, **other):
    print("x:", x, "y:", y, ",keys in 'other':",list(other.keys()))
    otherTotal = 0
    for k in list(other.keys()):
        otherTotal = otherTotal + other[k]
    print("The total of values in 'other' is", otherTotal)



print(maximum(34, 56, 11, 99, 7))
print(exampleFun( "book", "pizza", a=1, b=2, c=345 ))