
class Employee(object):

    raise_amount = 1.1  #1 클래스 변수 정의

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first.lower() + '.' + last.lower() + '@schoolofweb.net'

    def full_name(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)  #2 클래스 변수 사용

emp_1 = Employee('Sanghee', 'Lee', 50000)
emp_2 = Employee('Minjung', 'Kim', 60000)

print((emp_1.pay))      # 기존 연봉
emp_1.apply_raise()  # 인상률 적용
print((emp_1.pay))      # 오른 연봉
emp_1.pay = 0

print(("emp_1.__dict__\n", emp_1.__dict__))  # 인스턴스의 네임스페이스 참조
print("\n\n")
print(("Employee.__dict__ \n", Employee.__dict__))  # 클래스의 네임스페이스 참조