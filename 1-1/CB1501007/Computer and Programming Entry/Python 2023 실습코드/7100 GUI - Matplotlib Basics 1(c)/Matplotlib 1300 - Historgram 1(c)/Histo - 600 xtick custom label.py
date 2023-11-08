#-*- coding: cp949 -*-
# Name:        module1
# Author:      Zoh
# Created:     15-12-2018
#-------------------------------------------------------------------------------

"""
===========================
Rotating custom tick labels
===========================

Demo of custom tick-labels with user-defined rotation.
"""
import matplotlib.pyplot as plt


x = [1, 3, 4, 6]
y = [1, 4, 9, 6]
x2 = [2.562, 3, 7, 9]
y2 = [4, 3, 6.456, 7]
labels = ['Frogs', 'Hogs', 'Bogs', 'Slogs']

plt.plot(x, y, 'r--')
plt.plot(x2, y2, color='green', ls='-')

plt.xticks(x, labels, rotation='vertical', color="blue", size=15)

plt.margins(0.2)

plt.subplots_adjust(bottom=0.25)
plt.show()

