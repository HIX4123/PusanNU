
sa = set( list("computer"))
print("sa=", sa )

A = set([ frozenset([1,2]), frozenset([2,3]) ])
print(A)
print("len(A)=", len(A))

A.add(99)
print(A)
print("len(A)=", len(A))

# Bigs = { 1, 3, sa }
# 이것 이것 안됨.... set안의 원소로는 모두 immutable 한 것


