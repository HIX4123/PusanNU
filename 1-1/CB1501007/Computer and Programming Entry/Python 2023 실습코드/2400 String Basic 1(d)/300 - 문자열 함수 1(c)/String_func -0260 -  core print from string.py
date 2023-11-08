#-------------------------------------------------------------------------------
# Purpose:     2019 Power Python
# Author:      Cho
#-------------------------------------------------------------------------------

# Python3 code to demonstrate
# avoiding printing last comma
# using join()

# initializing list
test_list = ['Geeks', 'For', 'Geeks']

# printing original list
print ("The original list is : " + str(test_list))

# using join()
# avoiding printing last comma
print ("The formatted output is : ")
print (', '.join(test_list))
