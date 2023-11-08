#-------------------------------------------------------------------------------
# Purpose:     2019 Power Python
# Author:      Cho
#-------------------------------------------------------------------------------
from numpy import *
import networkx as nx
import matplotlib.pyplot as plt

N = 10
G = nx.grid_2d_graph(N,N)

posx=nx.spring_layout(G, iterations=200)

#plt.figure()
nx.draw_networkx( G, pos=posx, with_labels=False, node_color='y', node_size = 100)
plt.axis('off')
plt.show()