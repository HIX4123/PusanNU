

import graphviz as gv

g2 = gv.Digraph(format='pdf')
g2.node_attr['fontname'] = 'NanumMyeongjo' #NanumGothic
g2.node_attr['fontsize'] = '10.0'
g2.edge_attr['fontname'] = 'gulim.ttc'
g2.edge_attr['fontsize'] = '5.0'
g2.attr(layout='circo')

g2.node('닭')
g2.node('말')
g2.node('소')
g2.node('양')

g2.edge('닭', '말', color="red", label="수식")
g2.edge('말', '양', color="blue", label="가을")
g2.edge('양', '소', color="green", label="Winter")
g2.edge('닭', '소', color="black", label="여름")
g2.edge('소', '말', color="gray", style="dashed", label="f(x,y)")


#filename2 = g2.render(filename='chocho')
#print filename2

g2.view()



