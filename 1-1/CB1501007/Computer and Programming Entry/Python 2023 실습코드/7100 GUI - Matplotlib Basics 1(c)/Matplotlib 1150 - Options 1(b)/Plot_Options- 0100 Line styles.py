
import matplotlib.pyplot as plt

mycolor = 'cornflowerblue'
plt.plot([1, 2, 3, 8], [1, 4, 9, 16],  marker='o', linestyle="-.",  color=mycolor, linewidth=3)
plt.plot([1, 2, 5, 7], [7, 11, 3, 5] , linestyle="--",  color="red")
plt.plot([2, 3, 6, 9], [3, 6, 12, 10] ,  marker='D', linestyle="-",  color="black", linewidth=2)

plt.ylabel('some numbers')
plt.show()