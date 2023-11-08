
import matplotlib.pyplot as plt

plt.plot([1, 2, 3, 4], [1, 4, 9, 16],  color='green', marker='o',\
         linestyle='dashed',  linewidth=3, markersize=12,  alpha=.5)

plt.plot([1, 2, 3, 4], [8, 3, 2, 11],  color='tomato', marker='o',\
         linestyle='dotted',  linewidth=3, markersize=12,  alpha=.5)
# {dotted, dashed, dashdot, }


plt.ylabel('Line Styles Show')
plt.show()