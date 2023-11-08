#-------------------------------------------------------------------------------
# Purpose:     2019 Power Python
# Author:      Cho
#-------------------------------------------------------------------------------
C="""
    _single_leading_underscore: 주로 한 모듈 내부에서만 사용하는 private
    클래스/함수/변수/메서드를 선언할 때 사용하는 컨벤션이다.
    이 컨벤션으로 선언하게 되면 from module import *시 _로 시작하는 것들은
    모두 임포트에서 무시된다.
    그러나, 파이썬은 진정한 의미의 private을 지원하고 있지는 않기 때문에
    private을 완전히 강제할 수는 없다.
    즉, 위와 같은 임포트문에서는 무시되지만 직접 가져다 쓰거나 호출을 할
    경우엔 사용이 가능하다.
    그래서 “weak internal use indicator”라고 부르기도 한다.
"""
_internal_name = 'one_module' # private 변수
_internal_version = '1.0' # private 변수

class _Base: # private 클래스 _hidden_factor = 2 # private 변수
  def __init__(self, price):
      self._price = price

  def _double_price(self): # private 메서드
      return self._price * self._hidden_factor

  def get_double_price(self):
      return self._double_price()



print(" _internal_name=", _internal_name )

print(" _internal_version=", _internal_version )