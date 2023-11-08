# Frozenset 2개를 만들어 봅시다.

La=list("computer")
Lb=list("computer")
Lc=list("cuterompomp")

A = frozenset( La)
B = set( Lb)
C = frozenset( Lc)

print(f" A == B : {A==B}" ) # 내용만 비교

print(f" A == C : {A==C}" ) # 내용만 비교

print(f" type(A) == type(B) : {type(A) == type(B)}" )
print(f" type(A) == type(C) : {type(A) == type(C)}" ) # 내용만 비교

print(f" A is B = {A is B}" ) # 개체 그 자체를 비교
print(f" A is C = {A is C}" ) # 개체 그 자체를 비교
