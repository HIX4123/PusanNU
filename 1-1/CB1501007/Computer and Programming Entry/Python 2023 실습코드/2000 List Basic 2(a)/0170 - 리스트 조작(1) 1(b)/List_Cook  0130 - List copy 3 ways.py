
import copy

list1 = ["a", "b", "c"]
list2 = ["A", "B", "C", "D"]
list3 = [ "1", "2", "3", "4" ]
list1.append(list2)
list3.extend(list2)

print("원래 list1:",list1)
print("원래 list2:",list2)
print("원래 list3:",list3)

result1 = list1[:]
result2 = list(list1)
result3 = copy.copy(list1)
result4 = copy.deepcopy(list1)

print("\n붙인 결과 : ")
print("list1[:]\t\t\t\t", result1)
print("list(list1)\t\t\t\t", result2)
print("copy.copy(list1)\t\t", result3)
print("copy.deepcopy(list1)\t", result4)


print("\nlist1을 바꿨을 때")
list1.append("list1.append")
list2.append("list2.append")
print("바뀐 list1\t\t\t\t", list1)
print("list1[:]\t\t\t\t", result1)
print("list(list1)\t\t\t\t", result2)
print("copy.copy(list1)\t\t", result3)
print("copy.deepcopy(list1)\t", result4)

