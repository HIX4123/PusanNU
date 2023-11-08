


import matplotlib.pyplot as plt
import numpy as np
plt.style.use('seaborn-white')

for i in range(1, 7):
    plt.subplot(2, 3, i)
    plt.text(0.5, 0.5, str((2, 3, i)),
             fontsize=18, ha='center')


plt.show()