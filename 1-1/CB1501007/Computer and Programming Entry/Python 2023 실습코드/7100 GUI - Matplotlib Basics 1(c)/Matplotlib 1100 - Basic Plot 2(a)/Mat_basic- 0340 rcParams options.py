#-------------------------------------------------------------------------------
# Purpose:     2019 Power Python
# Author:      Cho
#-------------------------------------------------------------------------------

import matplotlib.pylab as plt


plt.rcParams["figure.figsize"] = (7,5)
plt.rcParams['lines.linewidth'] = 2
plt.rcParams['lines.color'] = 'r'
#plt.rcParams['axes.grid'] = True

data = [10, 24, 30, 50, 40]
plt.plot(data, alpha=0.4, color='k', marker='o')
plt.show()
