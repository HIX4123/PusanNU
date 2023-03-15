# difference between
# == and is operator
# [] is an empty list

list1 = []
list2 = []
list3 = list1


print(f"list1 == list2 : {list1 == list2}  ")


print(f"list1 is list2 : {list1 is list2}  ")

print(f"list1 is list3 : {list1 is list3}  ")


list3 = list3 + list2

print(f"list1 is list3 : {list1 is list3}  ")