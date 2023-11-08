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
import array as arr

print( "i   array   list ")

for i in range(0, 100, 5):
     test = [1.0*j for j in range(i)]
     a = arr.array('f', test)
     print(f"{i:3} | {sys.getsizeof(a):4} | {sys.getsizeof(test):4}")
