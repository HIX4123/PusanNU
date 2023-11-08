#-------------------------------------------------------------------------------
# Purpose:     2022 Zoh's Work     "過猶不及" 메롱..
# Author:      Cho
# Created:     2022-05-07
#-------------------------------------------------------------------------------


# len()         Return the length (the number of items) in the set.
# max()         Return the largest item in the set.
# min()         Return the smallest item in the set.
# sorted()      Return a new sorted list from elements in the set(does not sort the set itself).
# sum()         Retrun the sum of all elements in the set.


sa={3,4,5, 6, 7, 9, 10,23, -14}

print(f" len()= {len(sa)}")
print(f" max()= {max(sa)}")
print(f" sum()= {sum(sa)}")
print(f" min()= {min(sa)}")

mx=sorted(sa)
print(f" set sa = {sa }")
print(f" set mx = {mx }")
print(f" type(mx)= {type(mx)}")

for w in mx :
    print("=> ",w)