# 문자열을 정수 기준으로 정렬할 수 있다.

list1 = ["199","21", "10","3","22","23","4","2","200"]
list2 = [int(x) for x in list1]


list1.sort(key=int)
list2.sort()

print("list1=", list1)
print("list2=", list2)