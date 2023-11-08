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

numbers_list = [2, 5, 62, 5, 42, 52, 48, 5]

numbers_array = arr.array('i', numbers_list)

print(numbers_array[2:5]) # 3rd to 5th
print(numbers_array[:-5]) # beginning to 4th
print(numbers_array[5:])  # 6th to end
print(numbers_array[:])   # beginning to end