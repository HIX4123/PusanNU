
#% gviz -m layouts
# Layouts:
#  circo, dot, fdp, neato, nop, nop1, nop2, osage, patchwork, sfdp, twopi
#  See this http://melborne.github.io/2013/04/02/graphviz-layouts/

import graphviz as gv


# 2개의 그래프를 만들어 보시다. 하나는 단순 그래프, 다른 하나는 방향 그래프

g1 = gv.Graph(format='jpg')
g1.node_attr['fontname'] = 'Lucida Sans' #NanumGothic
g1.attr(layout='dot') # circo, dot, fdp, neato, nop, nop1, nop2, osage, patchwork, sfdp, twopi
# g1.attr(layout='circo')

vlabel=[]
N = 11
for x in range(N) :
    vlabel.append( str(x))


print vlabel


# edge를 추가함
for x in range(N):
    g1.edge( vlabel[x], vlabel[(x+1)%N], label=str(x)+"-"+str((x+1)%N))
    g1.edge( vlabel[x], vlabel[(x+2)%N], label=str(x)+"-jump")




g1.view()



