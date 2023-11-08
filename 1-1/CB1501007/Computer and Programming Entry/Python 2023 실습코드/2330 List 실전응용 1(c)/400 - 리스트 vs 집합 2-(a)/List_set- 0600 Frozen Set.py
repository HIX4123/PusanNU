
# Frozenset is a new class that has the characteristics of a set, but its elements cannot be changed once assigned. While tuples are immutable lists, frozensets are immutable sets.
# Sets being mutable are unhashable, so they can't be used as dictionary keys. On the other hand, frozensets are hashable and can be used as keys to a dictionary.


A = frozenset([1, 2, 3, 4])
B = frozenset([3, 4, 7, 9])


print(A.union(B))

print(A.isdisjoint(B))

print(A.difference(B))
print(A | B)


# A.add(3) # Oh ! No.... because it is frozen
