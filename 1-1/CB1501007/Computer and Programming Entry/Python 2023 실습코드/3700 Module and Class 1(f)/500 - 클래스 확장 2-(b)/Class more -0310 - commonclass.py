
# Purpose: 클래스의 특징 이해하기

class Employee:
   '공통 기본 베이스 클래스 for all employees' # Class String - 나중에 쓰인다.
   empCount = 0

   def __init__(self, name, salary): # 구성자(Constructor)
      self.name = name
      self.salary = salary
      Employee.empCount += 1

   def displayCount(self):
     print("Total Employee %d" % Employee.empCount)

   def displayEmployee(self):
      print("Name : ", self.name,  ", Salary: ", self.salary)

# 먼저 고용자(Employee) Class를 인스턴스화 해 봅시다.
data1 = Employee("Tuco",      3500 )
data2 = Employee("Mario",     6745 )
data3 = Employee("Esmeralda", 5400 )

data1.displayCount()
data2.displayEmployee()

# 새로운 instance 변수를 만들 수도 있다. 단 이것에 대한
# method( )는 정의가 되어있지 않다.
data1.Age = 43
data3.Age = 29
data3.Father = "John Parker"
print(data3.Age, data3.Father)
del data3.Age # 만든 instance를 없앨 수 도 있다.

print("\nAttribute를 출력합니다.")
print(hasattr(data1, 'Age'))    # Returns true if 'age' attribute exists
print(getattr(data1, 'Age'))    # Returns value of 'age' attribute
setattr(data1, 'Age', 8)       # Set attribute 'age' at 8
print(data1.Age)                # 다시 출력합니다.
print(delattr(data1, 'Age'))    # Delete attribute 'age'

print("\nBuilt-In Class 특성을 출력합니다.")
print("Employee.__doc__:", Employee.__doc__)
print("Employee.__name__:", Employee.__name__)
print("Employee.__module__:", Employee.__module__)
print("Employee.__bases__:", Employee.__bases__)

