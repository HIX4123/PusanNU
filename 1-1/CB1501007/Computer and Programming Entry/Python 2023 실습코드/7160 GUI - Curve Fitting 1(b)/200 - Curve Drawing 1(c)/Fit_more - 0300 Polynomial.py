
import numpy as np

x = np.array([0.0, 1.0, 2.0, 3.0,  4.0,  5.0])
y = np.array([0.0, 0.8, 0.9, 0.1, -0.8, -1.0])
z = np.polyfit(x, y, 3)
print("z=", z) # array([ 0.08703704, -0.81349206,  1.69312169, -0.03968254])


# 다항식으로 fitting을 해 봅시다.
p = np.poly1d(z)
print("3차 다항식으로 fitting")
print(p(0.5))    # 0.6143849206349179
print(p(3.5))    # -0.34732142857143039
print(p(10))     # 22.579365079365115


# 차수를 높이면 오히려 않좋을 수 있다. 룬게-메노이 현상
p30 = np.poly1d(np.polyfit(x, y, 30))
print(p30(4))    # -0.80000000000000204
print(p30(5))    # -0.99999999999999445
print(p30(4.5))  # -0.10547061179440398


# 어떻게 된 것인지 한번 그림으로 그려서 봅시다.
import matplotlib.pyplot as plt
plt.figure(figsize=(8, 6))
xp = np.linspace(-2, 6, 100)
plt.plot( x,        y,  'ro', label="Data")
plt.plot( xp,   p(xp),   '-', label="d= 3")
plt.plot( xp, p30(xp), 'g--', label="d=30")
plt.legend(loc='best')
plt.ylim(-2,3)
plt.show()

