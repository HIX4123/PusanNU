
import graphviz as gv

n1 = 'Apple'
g1 = gv.Graph (format='jpg')
g1.attr(bgcolor='yellow')
#g1.attr(fontname="gullim.ttc")

g1.node( n1 )
g1.node('Book')
g1.node('Coke')
g1.node('Dish')
g1.edge( n1, 'Book',label="0.2",)
g1.edge( n1, 'Dish', fontname="gulim.ttc", label="한글")
g1.edge( n1, 'Coke')
g1.edge('Coke', 'Dish', label="glabel")
print((g1.source))
g1.view()



