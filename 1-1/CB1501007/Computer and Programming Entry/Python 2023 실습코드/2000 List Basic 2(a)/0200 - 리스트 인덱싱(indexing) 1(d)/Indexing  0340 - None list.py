#-------------------------------------------------------------------------------
# Purpose:     2021 Prof. Zoh's Work     "착하게 살지 말자."
# Author:      Cho
# Created:     2021-05-03
#-------------------------------------------------------------------------------



# Create a length-N list of the same thing
# Use the Python list * operator:

four_nones = [None] * 4

print(f"four_nones= {four_nones}")

# Create a length-N list of lists
# Because lists are mutable,
# the * operator (as above) will create a list of N references to the same list, which is not likely what you want. Instead, use a list comprehension:

four_lists = [[] for __ in range(4)]

print(f"four_lists= {four_lists}")

