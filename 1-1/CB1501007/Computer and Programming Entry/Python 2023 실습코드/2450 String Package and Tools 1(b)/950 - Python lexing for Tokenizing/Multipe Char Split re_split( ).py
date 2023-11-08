
# Python3 code to demonstrate working of
# Splitting operators in String
# Using re.split()

import re


data = "GeeksforGeeks, is_an-awe     some ! website"

# Using re.split()
# Splitting characters in String
res = re.split(', |_|-|!', data)

# printing result
print("Result= ", res )