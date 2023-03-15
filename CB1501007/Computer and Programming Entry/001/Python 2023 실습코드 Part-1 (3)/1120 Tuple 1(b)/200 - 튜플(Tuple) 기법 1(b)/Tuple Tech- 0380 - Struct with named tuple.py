
from collections import namedtuple

MyStruct = namedtuple("MyStruct", "field1 field2 field3")
Myrecord = namedtuple("Cool", "Age Name Sex")


m1 = MyStruct("foo", "bar", "baz")
m2 = MyStruct(field1 = "foo", field2 = "bar", field3 = "baz")

print(m1)
print(m2.field2)

w1 = Myrecord(Age=32, Name="DogCat", Sex=0)
print(w1)
