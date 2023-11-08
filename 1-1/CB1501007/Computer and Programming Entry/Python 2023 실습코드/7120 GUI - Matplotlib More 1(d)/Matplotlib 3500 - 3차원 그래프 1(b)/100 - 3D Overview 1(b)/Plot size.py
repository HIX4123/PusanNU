#-------------------------------------------------------------------------------
# Author:      Zoh
# Created:     2020-05-05
#-------------------------------------------------------------------------------

# matplotlib inline
import matplotlib.pylab as plt

plt.rcParams["figure.figsize"] = (10,10)
plt.rcParams['lines.linewidth'] = 2
plt.rcParams['lines.color'] = 'r'
plt.rcParams['axes.grid'] = True

##plt.rcParams["figure.figsize"] = (10,4)
##plt.rcParams['lines.linewidth'] = 4
##plt.rcParams['lines.color'] = 'r'
##plt.rcParams['axes.grid'] = True

data = [10, 24, 30, 50, 40]
plt.plot(data)
plt.show()
