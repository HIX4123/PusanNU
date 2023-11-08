#--------------------------------------------------------
# Author:      Zoh Que
# Created:     07-02-2023
#--------------------------------------------------------

my_array = [["A", "B", "C", "D"],
           ["E", "F", "G", "H"],
           ["I", "J", "K", "L"],
           ["M", "N", "O", "P"]]


#my_slice2 = my_array[1:3, 0:2]   # Does not work !
#print(my_slice2)


import numpy
my_array = numpy.array(my_array)
my_slice2 = my_array[1:3, 0:2]
print(f"\n > my_array[1:3, 0:2] \n {my_slice2}")



my_slice2 = my_array[:2, :]
print(f"\n > my_array[:2, :] \n {my_slice2}")


my_slice2 = my_array[:, 2:]
print(f"\n > my_array[:, 2:] \n {my_slice2}")


my_slice2 = my_array[:, ::2]
print(f"\n > my_array[:, ::2] \n {my_slice2}")


my_slice2 = my_array[::2, ::2]
print(f"\n > my_array[::2, ::2] \n {my_slice2}")