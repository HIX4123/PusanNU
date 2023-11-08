
# 실험 4 - List에서 빼기 - delete와 remove

print("\n 실험 3 ")
x=["first", "second", "third", "fourh", "fifth", "sixth", "last"]
print("원본 ", x)

del x[1]        # delete는 해당되는 위치에 있는 것을 무조건 지운다.
print(x)
del x[-3:-1]
print(x)

x.append("third")
print(x)
x.remove("third")  # remove는 해당되는 원소를 찾아서 지운다.
print(x)
x.remove("third")
print(x)

