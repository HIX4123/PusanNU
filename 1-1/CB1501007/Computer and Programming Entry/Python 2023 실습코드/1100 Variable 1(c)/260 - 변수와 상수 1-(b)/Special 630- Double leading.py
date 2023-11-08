#-------------------------------------------------------------------------------
# Purpose:     2019 Power Python
# Author:      Cho
#-------------------------------------------------------------------------------

C="""
    __double_leading_underscores: 이는 컨벤션이라기보단 하나의 문법적인 요소이다.
    더블 언더스코어는 클래스 속성명을 맹글링하여 클래스간 속성명의 충돌을
    방지하기 위한 용도로 사용된다.
    (맹글링이란, 컴파일러나 인터프리터가 변수/함수명을 그대로 사용하지 않고
    일정한 규칙에 의해 변형시키는 것을 말한다.)
    파이썬의 맹글링 규칙은 더블 언더스코어로 지정된 속성명 앞에
    _ClassName을 결합하는 방식이다. 즉, ClassName이라는 클래스에서
    method라는 메서드를 선언했다면 이는 _ClassNamemethod로 맹글링 된다.
"""

class A:
  def _single_method(self):
      pass

  def __double_method(self): # 맹글링을 위한 메서드
      pass

class B(A):
  def __double_method(self): # 맹글링을 위한 메서드
      pass

print(dir(A())) # ['_A_double_method', ..., '_single_method']
print(dir(B())) # ['_A_double_method', '_B_double_method', ..., '_single_method']

  # 서로 같은 이름의 메서드를 가지지만 오버라이드가 되지 않는다.
