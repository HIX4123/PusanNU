

## c, coef, coefficients는 다항식의 계수를 반환합니다.
## 즉, [1, -3, 2]은 x^2 - 3x - 2가 되며, 앞선 예시의 equation2의
## 반환값과 같은 것을 확인할 수 있습니다.
##
## o, order는 다항식의 최고 차수를 반환합니다.
## 그러므로, 다항식의 최대 차수인 2를 반환합니다.
##
## r, roots는 다항식의 근을 반환합니다.
## 다항식에서 0이 되는 값인 [2, 1]을 반환합니다.
##
## variable은 다항식의 변수명을 반환합니다.
## 변수명을 별도로 입력하지 않았으므로, 기본값인 x를 반환합니다.
##


import numpy as np

equation = np.poly1d([1, 2], True)  # (x-1)(x-2)
print(equation.c, equation.coef, equation.coefficients)
print(equation.o, equation.order)
print(equation.r, equation.roots)
print(equation.variable)