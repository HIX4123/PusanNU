
list1 = ["199","21", "10","3","22","23","4","2","200"]
list2 = [int(x) for x in list1]
list2.sort()

list1.sort(key=int)
print(list1)