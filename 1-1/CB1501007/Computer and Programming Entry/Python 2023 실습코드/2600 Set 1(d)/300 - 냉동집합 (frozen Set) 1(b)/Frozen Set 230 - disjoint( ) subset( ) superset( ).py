# Frozenset 2개를 만들어 봅시다.

La=list("computer")
Lb=list("puterc")
Lc=list("pumco")

A = frozenset( La)
B = frozenset( Lb)
C = frozenset( Lc)

# isdisjoint() method
print(A.isdisjoint(C))  # Output: True

# issubset() method
print(C.issubset(B))  # Output: True

# issuperset() method
print(A.issuperset(C))  # Output: Truee(B)={A.symmetric_difference(B)}")  # Output: frozenset({1, 2, 5, 6})