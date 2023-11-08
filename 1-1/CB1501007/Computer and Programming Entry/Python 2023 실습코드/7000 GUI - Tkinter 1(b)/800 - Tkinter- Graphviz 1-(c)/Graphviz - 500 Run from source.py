
from graphviz import Source
path = 'smachine.dot'
s = Source.from_file(path)
s.view()


path = 'dtree.dot'
s2 = Source.from_file(path)
s2.view()


path = 'summary.dot'
s3 = Source.from_file(path)
s3.view()


path = 'dflow.dot'
s4 = Source.from_file(path)
s4.view()

