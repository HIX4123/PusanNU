#-------------------------------------------------------------------------------
# Purpose:     2019 Power Python
# Author:      Cho
#-------------------------------------------------------------------------------


from numpy import *
import networkx as nx
import matplotlib.pyplot as plt

N = 10
G = nx.grid_2d_graph(N,N)

pos = dict( (n, n) for n in G.nodes() )
labels = dict( ((i, j), i + (N-1-j) * N ) for i, j in G.nodes() )

nx.relabel_nodes(G,labels,False)
inds=labels.keys()
vals=labels.values()

inds = sorted(inds)
vals = sorted(vals)

print("\n inds=", inds)
print("\n vals=", vals)

pos2=dict(zip(vals,inds))
print("\n pos2=", pos2)

T = nx.minimum_spanning_tree(G)

#plt.figure()
nx.draw_networkx( T, pos=pos2, with_labels=False, node_color='y', node_size = 100)
plt.axis('off')
plt.show()