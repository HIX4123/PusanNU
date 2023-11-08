


import matplotlib.pyplot as plot

plot.figure(figsize=(8,5)) # 인치

X  = [  1,  2,  3,  4,   7]
Y1 = [  1,  4,  9, 16,  11]
Y2 = [ 25,  8, 13, 12,  28]
Y3 = [ 22, 11, 15, 10,  21]
mytrans=0.25
plot.plot( X, Y1, 'olive'   , marker='o', alpha=mytrans, linewidth=3)
#plot.plot( X, Y2, 'navy'    , marker='D', alpha=mytrans)
plot.plot( X, Y2, "o" )
plot.plot( X, Y3, 'tomato'  , marker='x', alpha=mytrans, linewidth=4)
plot.title(r'PNU  CSED is the Best One.')
plot.ylabel('Monthly Paying')
plot.xlabel('We are the World WoRLD!')
plot.show()

# marker https://matplotlib.org/3.1.1/api/markers_api.html