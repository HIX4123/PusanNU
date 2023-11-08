"""
Code 	C Type 	          Python Type 	Min bytes
-----------------------------------------------------
'b' 	signed char 	    int 	      1
'B' 	unsigned char 	    int 	      1
'u' 	Py_UNICODE 	        Unicode 	  2
'h' 	signed short 	    int 	      2
'H' 	unsigned short 	    int 	      2
'i' 	signed int 	        int 	      2
'I' 	unsigned int 	    int 	      2
'l' 	signed long 	    int 	      4
'L' 	unsigned long 	    int           4
'f' 	float 	            float 	      4
'd' 	double 	            float 	      8
"""

import array as arr

odd = arr.array('i', [1, 3, 5])
even = arr.array('i', [2, 4, 6])
numbers = arr.array('i')   # creating empty array of integer
numbers = odd + even

print(numbers)