"""
"." 	m00 	point
"," 	m01 	pixel
"o" 	m02 	circle
"v" 	m03 	triangle_down
"^" 	m04 	triangle_up
"<" 	m05 	triangle_left
">" 	m06 	triangle_right
"1" 	m07 	tri_down
"2" 	m08 	tri_up
"3" 	m09 	tri_left
"4" 	m10 	tri_right
"8" 	m11 	octagon
"s" 	m12 	square
"p" 	m13 	pentagon
"P" 	m23 	plus (filled)
"*" 	m14 	star
"h" 	m15 	hexagon1
"H" 	m16 	hexagon2
"+" 	m17 	plus
"x" 	m18 	x
"X" 	m24 	x (filled)
"D" 	m19 	diamond
"d" 	m20 	thin_diamond
"|" 	m21 	vline
"_" 	m22 	hline
0 (TICKLEFT) 	 m25 	tickleft
1 (TICKRIGHT) 	 m26 	tickright
2 (TICKUP) 	        m27 	tickup
3 (TICKDOWN) 	  m28 	tickdown
4 (CARETLEFT) 	 m29 	caretleft
5 (CARETRIGHT) 	    m30 	caretright
6 (CARETUP) 	   m31 	caretup
7 (CARETDOWN)   	m32 	caretdown
8 (CARETLEFTBASE) 	m33 	caretleft (centered at base)
9 (CARETRIGHTBASE) 	m34 	caretright (centered at base)
10 (CARETUPBASE) 	m35 	caretup (centered at base)
11 (CARETDOWNBASE) 	m36 	caretdown (centered at base)
"None", " " or "" 	  	nothing
'$...$' 	m37 	Render the string using mathtext. E.g "$f$" for marker showing the letter f.
verts 	  	A list of (x, y) pairs used for Path vertices. The center of the marker is located at (0,0) and the size is normalized, such that the created path is encapsulated inside the unit cell.
path 	  	A Path instance.
(numsides, style, angle)

The marker can also be a tuple (numsides, style, angle), which will create a custom, regular symbol.

numsides:
    the number of sides
style:

    the style of the regular symbol:

        0: a regular polygon
        1: a star-like symbol
        2: an asterisk
        3: a circle (numsides and angle is ignored); deprecated.

angle:
    the angle of rotation of the symbol
"""

# marker 점에 대해서만 다른 색을 지정한다.

import matplotlib.pyplot as plot

plot.figure(figsize=(8,5))
X  = [ 1, 2,  3,  4,  7]
Y1 = [ 1, 4,  9, 16, 11]
Y2 = [ 25, 8, 13, 12,  28]
plot.plot( X, Y1, 'red'   , marker='<', alpha=0.5)
plot.plot( X, Y2, 'orange', marker='>', \
           markerfacecolor='k', markeredgecolor='green', \
           alpha=0.5, linewidth=4)

plot.title(r'PNU CSED is the Best One.')
plot.ylabel('some numbers')
plot.show()

# marker https://matplotlib.org/3.1.1/api/markers_api.html

# markersize=5,
# markerfacecolor='w',\
# markeredgewidth=1.5,
# markeredgecolor=(r, g, b, 1))