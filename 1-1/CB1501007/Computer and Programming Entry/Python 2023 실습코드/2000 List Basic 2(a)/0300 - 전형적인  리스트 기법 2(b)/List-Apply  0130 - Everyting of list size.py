"""
Commonly used type codes are listed as follows:

Code   C Type 	        Python Type   Min bytes

b 		signed char 	int         1
B		unsigned char 	int 		1
u 		Py_UNICODE 		Unicode 	2
h		signed short	int			2
H		unsigned short	int			2
i		signed int		int			2
I		unsigned int	int   	    2
l 		signed long 	int 		4
L 		unsigned long 	int 		4
f		float    		float   	4
d 		double 			float 		8
"""
import sys
la = [ ]
lb = [ ]
print ( ">1 ", sys.getsizeof( la ) )
la.append(9999)
print ( ">2 ", sys.getsizeof( la ) )
print ( ">3 ", sys.getsizeof( lb ) )
lb.append("Summer Time")
print ( ">4 ", sys.getsizeof( lb ) )
print ( ">5 ", sys.getsizeof( [] ) )
print ( ">6 ", sys.getsizeof( [1] ) )

