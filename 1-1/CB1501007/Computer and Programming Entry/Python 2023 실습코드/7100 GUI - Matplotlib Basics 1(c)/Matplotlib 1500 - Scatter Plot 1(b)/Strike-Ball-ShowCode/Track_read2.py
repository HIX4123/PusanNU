#-------------------------------------------------------------------------------
# Author:      Zoh
# Created:     2019-07-06
#-------------------------------------------------------------------------------


import csv
import matplotlib.pyplot as plt


from matplotlib.pyplot import figure
figure(num=None, figsize=(8, 7), facecolor='w', edgecolor='k') #dpi=100,


f = open('Ball.csv', 'r')
rdr = csv.reader(f)
heading = next( rdr)
print("cvs_head=", heading )

Tcolumn=["PitchCall", "PlateLocHeight","PlateLocSide" ]
bcall   = heading.index(Tcolumn[0])
bheight = heading.index(Tcolumn[1])
bside   = heading.index(Tcolumn[2])
print("bcall, bheight, bside= ", bside, bheight, bside)

count=0
Call=[]
Ypoint=[]
Xpoint=[]
for line in rdr:
    count+=1
    Call.append( line[bcall])
    Ypoint.append( float(line[bheight]) )
    Xpoint.append( float( line[bside] ) )


bsize= 11
scount = bcount = 0
for (c,x,y) in zip(Call, Xpoint, Ypoint):
    #print(c,x,y)
    if c == "StrikeCalled" :
        scount += 1
        plt.plot(x,y, color='blue',  alpha=.5,  marker='o', markersize=bsize)
    if c == "BallCalled" :
        bcount += 1
        plt.plot(x,y, color='tomato',  alpha=.5, marker='o', markersize=bsize )


plt.ylabel('Ball height')
ltext='[Strike, Ball] = '+"["+ str(scount)+ "," + str(bcount)+"]"
plt.xlabel( ltext)
plt.axis('scaled')
plt.plot(0,0, 'go', label=ltext)
plt.legend( )
plt.show()

f.close()
