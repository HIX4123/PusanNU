

from graphviz import Source


tmp="""
graph {
    a -- b -- d -- c -- f[color=red,penwidth=3.0];
    b -- c;
    d -- e;
    e -- f;
    a -- d;
}



"""

s = Source(tmp, filename="path.gv", format="png")
s.view()



