
# Purpose: return value를 살펴보기
# 하나를 돌려주는 경우
def inc(x):
    return x + 1

foo = 10
foo = inc(foo)
print(foo)


def times(x, y):      # create and assign function
     return x * y      # body executed when called
# --------- end of times( ) ----------


x = times(3.14, 4)    # save the result object
print("times() = ", x)




# 여러 개를 돌려주는 경우
def next_block():
    p1 = 2
    p2 = 2.3
    p3 = "c"
    p4 = "String"
    p5 = "3.4444"
    return p1, p2, p3, p4, p5  #이것은 tuple이다. list가 아니라.
# --------- end of next_block( ) ----------


myval = next_block() # 주의 주의!!!!

print("\n myval = ", myval, end=' ')
print("\n myval[1] = ", myval[1])





