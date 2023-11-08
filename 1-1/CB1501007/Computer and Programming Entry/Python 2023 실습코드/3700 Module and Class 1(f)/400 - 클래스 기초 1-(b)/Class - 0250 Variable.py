
# class03.py

class Var:
    c_mem = 100                 # 클래스 변수
    def f(self):
        self.i_mem = 200        # 멤버 변수
    def g(self):
        print((self.i_mem))
        print((self.c_mem))



print(("Var.c_mem =" ,Var.c_mem))
#print(("Var.c_mem =" ,self.i_mem))
