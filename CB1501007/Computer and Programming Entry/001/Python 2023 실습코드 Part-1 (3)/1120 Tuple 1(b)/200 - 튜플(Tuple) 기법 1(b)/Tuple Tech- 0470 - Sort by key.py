#-------------------------------------------------------------------------------
# Purpose:     2019 Power Python
# Author:      Cho
#-------------------------------------------------------------------------------


tuples = [('Kim',34), ('Han',64), ('Moon',29), ('Han',27), ('Moon', 52)]

def age(t):
    return t[1]

def name(t):
    return t[0]

tuples.sort(key=age)
print("key=age", tuples)

tuples.sort(key=name)
print("key=name", tuples)



