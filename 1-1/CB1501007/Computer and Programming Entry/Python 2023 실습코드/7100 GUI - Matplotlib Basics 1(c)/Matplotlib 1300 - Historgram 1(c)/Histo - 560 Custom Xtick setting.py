
import matplotlib.pyplot as plt
import numpy as np


valueX =   [-3, 1, 2, 3, 4]
scoreList = [2, 5, 0, 6, 2]

plt.plot(valueX, scoreList)
plt.xlabel("Score number") # Text for X-Axis
plt.ylabel("Score") # Text for Y-Axis
plt.title("Scores for the topic ")

#plt.xticks([1,2,3,4])
#plt.xticks(list(range(-3, 8)))
plt.xticks([1,3,5,6,7])


plt.show()