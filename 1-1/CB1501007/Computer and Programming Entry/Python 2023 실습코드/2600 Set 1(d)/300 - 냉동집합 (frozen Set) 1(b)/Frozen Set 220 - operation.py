# Frozenset 2개를 만들어 봅시다.

A = frozenset([1, 2, 3, 4])
B = frozenset([3, 4, 5, 6])

# 복사할 때는 member function .copy( )를 사용해야 합니데이.

C = A.copy()  # Output: frozenset({1, 2, 3, 4})
print(f"C={C}, C의 type={type(C)}")

# 냉동집합을 union을 하는 방법
print(f"A.union(B)={A.union(B)}")  # Output: frozenset({1, 2, 3, 4, 5, 6})


print(f"A.intersection(B)={A.intersection(B)}")  # Output: frozenset({3, 4})

# difference
print(f"A.difference(B)={A.difference(B)}")  # Output: frozenset({1, 2})

# symmetric_difference
print(f"A.symmetric_difference(B)={A.symmetric_difference(B)}")  # Output: frozenset({1, 2, 5, 6})