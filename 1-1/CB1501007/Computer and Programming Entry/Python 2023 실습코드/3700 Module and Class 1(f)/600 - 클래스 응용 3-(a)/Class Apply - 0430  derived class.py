


class Base:
    def f(self):
        self.g()                # ?⑥닔 g() ?몄텧
    def g(self):
        print('Base')

class Derived(Base):
    def g(self):                # ?뚯깮 ?대옒?ㅼ쓽 ?⑥닔 g()
        print('Derived')

b = Base()
b.f()           # Base??g() ?몄텧

a = Derived()
a.f()           # Derived??g() ?몄텧
