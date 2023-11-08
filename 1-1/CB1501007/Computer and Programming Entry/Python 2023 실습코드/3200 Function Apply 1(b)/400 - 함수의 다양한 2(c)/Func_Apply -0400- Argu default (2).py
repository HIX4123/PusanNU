
print("\n실험-02 ----------")
i = 5
def f( arg=i ): # i값이 언제 결정되는지를 잘 봅시다.
    print(arg)

i = 6
f()

# Default Argument Values: default value is evaluated only once
# 수정가능한 객체가 passing되면 argument는 그 값이 선언될 때
# 이전의 값을 그대로 유지하게 된다. 즉 list나 dictionary인 경우
# For example, the following function
# accumulates the arguments passed to it on subsequent calls:

print("\n실험-02 ----------")
def f(a, L=[]):
    L.append(a)
    return L

print(f(1))
print(f(2))
print(f(3))
