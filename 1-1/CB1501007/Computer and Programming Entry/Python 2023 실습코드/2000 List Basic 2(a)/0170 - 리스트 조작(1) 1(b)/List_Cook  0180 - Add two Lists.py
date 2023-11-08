
import numpy as np



first = [1, 2, 3, 4]
second = [2, 3, 4, 5]
third = list(map(sum, list(zip(first, second))))
print(third)



fourth = [first[i]+ second[i]+100 for i in range(len(first))]
print(fourth)

fifth = np.add(first, second)
print(fifth)

tenth = list(map(lambda x,y: x+y+300,first,second))
print(tenth)