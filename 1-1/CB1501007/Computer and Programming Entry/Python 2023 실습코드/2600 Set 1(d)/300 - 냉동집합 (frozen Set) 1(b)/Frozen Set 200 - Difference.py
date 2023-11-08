#-------------------------------------------------------------------------------
# Purpose:     2019 Power Python
# Author:      Cho
#-------------------------------------------------------------------------------


# There are currently two builtin set types, set and frozenset.
# The set type is mutable -- the contents can be changed using
# methods like add() and remove(). Since it is mutable,
# it has no hash value and cannot be used as either a dictionary key
# or as an element of another set.

# The frozenset type is immutable and hashable
# -- its contents cannot be altered after is created; however,
# it can be used as a dictionary key or as an element of another set.

# 언집합(frozen set)은 일단 만들어지면 추가 삭제가 불가능하다. 그러나
# frozen set은 이 특징때문에 hashing의 키가 될 수 있다. 변화가 없으므로
# {a, b, c} , {b, c, e}를 각각 hashing의 key가 될 수 있다.


# creating a dictionary
Student = {"name": "Ankit", "age": 21, "sex": "Male",
           "college": "MNNIT Allahabad", "address": "Allahabad"}

# making keys of dictionary as frozenset
key = frozenset(Student)

# printing keys details
print('The frozen set is:', key)

myciti = set((("Python","Perl"), ("Paris", "Berlin", "London")))
# yourciti = set((["Python","Perl"], ["Paris", "Berlin", "London"]))
#  위와 같이는 선언이 될 수 없다. 왜냐하면 set의 원소는 list가 불가능함.

tciti = set(["Frankfurt", "Basel","Freiburg"])
tciti.add("Strasbourg")
print("theyciti= ", tciti )

wciti = frozenset(["Frankfurt", "Basel","Freiburg"])
# wciti.add("Strasbourg")
# 이것은 불가능함.

# set의 모든 원소는 빠른 탐색이 가능하도록 immutable이 되어야 한다.
# 즉 각 원소는 중간에 변화를 주면 안된다. 그러면 hash가 깨어지기 때문에

# set7={ 5, 1, 9, (1,2,3), range(7), {1,2,3}}  #안됨. {1,2,3}은 mutable이므로
set7={ 5, 1, 9, (1,2,3), range(7), frozenset({1,2,3})}


print("set7=", set7 )
for w in set7 :
    print(w)

