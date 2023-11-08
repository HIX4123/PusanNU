
from operator import itemgetter

class Student:
	def __init__(self, name, grade, age):
		self.name = name
		self.grade = grade
		self.age = age
	def __repr__(self):
		return repr((self.name, self.grade, self.age))

# a list of custom objects
L = [Student('Bob', 'B', 30),
	 Student('Sam', 'A', 35),
     Student('Max', 'B', 25),
     Student('Tom', 'A', 20),
	 Student('Sam', 'B', 32),
     Student('Max', 'C', 15),
     Student('Tom', 'B', 28),
     Student('Ron', 'A', 40),
     Student('Ben', 'B', 15)]


Lx = sorted(L, key=lambda student: student.age)
for w in Lx :
    print(w)

from operator import attrgetter
print("\n from operator import attrgetter <<")
Lx = sorted(L, key=attrgetter('grade', 'age'))
for w in Lx :
    print(w)