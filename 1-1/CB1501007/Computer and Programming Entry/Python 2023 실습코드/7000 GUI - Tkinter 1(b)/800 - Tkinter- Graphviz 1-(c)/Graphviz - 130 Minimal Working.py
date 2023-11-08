

import graphviz as gv

g1 = gv.Graph(format='jpg')
g1.node('Apple')
g1.node('Book')
g1.node('Coke')
g1.node('Dish')
g1.edge('Apple', 'Book')
g1.edge('Apple', 'Dish')
g1.edge('Apple', 'Coke')
g1.edge('Coke', 'Dish')
print(g1.source)
g1.view()

filename = g1.render(filename='sg')
print (filename)

g2 = gv.Digraph(format='jpg')
g2.node('A')
g2.node('B')
g2.node('C')
g2.node('D')
g2.edge('A', 'B')
g2.edge('A', 'C')
g2.edge('B', 'C')
g2.edge('B', 'D')
filename2 = g2.render(filename='dgg')
print (filename2)

g2.view()



