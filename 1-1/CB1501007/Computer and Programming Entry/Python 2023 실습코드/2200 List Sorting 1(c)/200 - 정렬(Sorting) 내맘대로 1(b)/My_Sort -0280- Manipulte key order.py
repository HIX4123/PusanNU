#-------------------------------------------------------------------------------
# Purpose:     2020 Prof. Zoh's Work
# Author:      Cho
# Created:     2020-10-13
#-------------------------------------------------------------------------------


l = [["d", 5], [ "e", 10], [ "a", 5],["d", 6], [ "e", 7], [ "a", 8] ]

# copy
l_sorted = sorted(l, key=lambda x: (x[0], x[1]*-1))
print("l_sorted[]= ", l_sorted )

# in place
l.sort(key=lambda x: (x[0], x[1]*-1) )
print("l[]= ", l )