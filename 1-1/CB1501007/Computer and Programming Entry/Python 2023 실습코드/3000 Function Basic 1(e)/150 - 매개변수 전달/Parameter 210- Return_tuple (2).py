

# 여러 개의 값의 tuple로 return해주는 함수
def banana(x,y):
    myr = (x+y, x-y, x*y, x/y) # 4개 묶음
    return (myr)




a=134
b=33

rval= banana(a,b)

print(rval)
print("first item= ", rval[0], rval[-1])


#rval[1]=3 #은 수행되지 않는다. tuple은 변경불가!!!
# tuple object does not support assignment

# 세상에는 10가지 사람들이 있다.
# 이진수를 이해하는 사람과 아닌 사람.