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

import array as arr
a = arr.array('d', [1.1, 3.5, 4.5])
print(a)


b = arr.array('B', [11, 12, 23, 45, 0 ] )
print(b)

c =arr.array('l')
d =arr.array('u', 'hello \u2641')
e =arr.array('l', [1, 2, 3, 4, 5])
f =arr.array('d', [1.0, 2.0, 3.14])