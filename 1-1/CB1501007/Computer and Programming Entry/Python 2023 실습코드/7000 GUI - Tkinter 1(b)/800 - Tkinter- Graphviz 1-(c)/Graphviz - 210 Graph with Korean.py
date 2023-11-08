# See this site https://www.tonyballantyne.com/graphs.html
import graphviz as gv

n1 = 'Apple'
g1 = gv.Digraph (format='jpg')          # g1 = gv.Graph (format='jpg')
g1.attr( bgcolor='lightyellow')

#g1.graph_attr['rankdir'] = 'LR'
g1.node_attr['shape']       = 'box'
g1.node_attr['fontname']    = 'Arial'
g1.node_attr['fontsize']    = '12'
g1.node_attr['style']       = 'filled'
g1.node_attr['margin']      = '0.1'
g1.node_attr['height']      = '0.4'
g1.node_attr['fillcolor'] = '#fff7da'

#g1.edge_attr['style'] = 'dashed'


g1.node( n1, style="filled", fillcolor="red")
g1.node('Book', style="filled", fillcolor="green")
g1.node('Coke')
g1.node('Dish')
g1.edge( n1, 'Book', fontname="NanumGothic.ttc", fontsize="12.0", label= u"어 한글이 되네" )
g1.edge( n1, 'Dish', label= "Pizza", style='dashed' )
g1.edge( n1, 'Coke', label="MyMy", fontcolor="red", fontsize="18.0" )
g1.edge('Coke', 'Dish', label="23.167")
g1.edge( 'Book', 'Dish', label="-100")

#print(g1.source)

g1.view()



