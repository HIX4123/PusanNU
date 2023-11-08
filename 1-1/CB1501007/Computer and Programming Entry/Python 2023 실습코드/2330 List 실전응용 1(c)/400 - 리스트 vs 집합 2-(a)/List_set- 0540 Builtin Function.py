
# all()         Return True if all elements of the set are true (or if the set is empty).
# any()         Return True if any element of the set is true. If the set is empty, return False.
# enumerate()   Return an enumerate object. It contains the index and value of all the items of set as a pair.
# len()         Return the length (the number of items) in the set.
# max()         Return the largest item in the set.
# min()         Return the smallest item in the set.
# sorted()      Return a new sorted list from elements in the set(does not sort the set itself).
# sum()         Retrun the sum of all elements in the set.


sa = { 56, "good", 563, 5, 7, 11, 54.34, "Text" }
sb = { "a", "g", "t", "m", False }


print(all(sa), all(sb))

for i,x in enumerate(sa):
    print(i, x)