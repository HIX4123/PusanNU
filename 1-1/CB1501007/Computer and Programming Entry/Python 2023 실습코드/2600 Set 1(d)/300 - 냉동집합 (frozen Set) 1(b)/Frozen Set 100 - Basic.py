
# 일반적으로 set은 삽입 삭제가 가능한 mutable 자료형이므로
# 이것은 dict에 사용할 수 없다.
# 이것을 가능하게 하는 것인 꽁꽁-얼린 냉동집합, frozen set이다.

# The frozenset() method returns an immutable frozenset
# initialized with elements from the given iterable.
# If no parameters are passed, it returns an empty frozenset.

# tuple of vowels
vowels = set(('a', 'e', 'i', 'o', 'u'))
conso  = set("rdgtykz")
print("vowels=", vowels )
print("conso =", conso )

fSet = frozenset(vowels)
print( fSet)
print( "empty fset()=", frozenset())

conso.add('q')
print(conso)
#fSet.add('x')