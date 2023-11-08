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

number = arr.array('i', [1, 2, 3, 3, 4])

del number[2]   # removing third element
print(number)   # Output: array('i', [1, 2, 3, 4])

del number      # deleting entire array
#print(number)   # Error: array를 이미 지워졌기 때문이다.


numbers = arr.array('i', [10, 11, 12, 12, 13])
numbers.remove(12)
print(numbers)   # Output: array('i', [10, 11, 12, 13])
print(numbers.pop(2))   # Output: 12
print(numbers)   # Output: array('i', [10, 11, 13])