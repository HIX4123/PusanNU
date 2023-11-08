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
numbers = arr.array('i', [1, 2, 3, 5, 7, 10])


numbers[0] = 0
print(numbers)

numbers[2:5] = arr.array('i', [4, 6, 8])
print(numbers)


# Output: array('i', [0, 2, 4, 6, 8, 10])