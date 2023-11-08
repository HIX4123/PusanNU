

import graphviz as gv


# 2개의 그래프를 만들어 보시다. 하나는 단순 그래프, 다른 하나는 방향 그래프

g1 = gv.Graph(format='jpg')
g1.node_attr['fontname'] = 'Lucida Sans' #NanumGothic
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

g2 = gv.Digraph(format='png')
g2.node_attr['fontname'] = 'NanumMyeongjo' #NanumGothic
g2.node('달')
g2.node('소나무')
g2.node('토끼')
g2.node('할머니')
g2.node('선녀 a')
g2.edge('달', '소나무')
g2.edge('달', '할머니')
g2.edge('달', '토끼')
g2.edge('소나무', '토끼', '선녀')
g2.edge('소나무', '선녀 a')
filename2 = g2.render(filename='chocho')
print (filename2)

g2.view()



