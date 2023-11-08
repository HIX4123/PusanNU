#-------------------------------------------------------------------------------
# Author:      Zoh
# Created:     2021-03-28
#-------------------------------------------------------------------------------

L = [(14, 2, 3), (1, 14, 0), (14, 1, 1), (1, 14, 2), (2, 4, 4),
     (11, 23, 5), (4, 11, 5), (5,5,5), (32, 21, 4), (11, 23, 6)]
M = sorted(L)

print("\n M=")
for w in M : print(w)

# The t[::-1] uses a reversing slice.
"""
where the lambda returns a reversed tuple to sort on
instead. The callable object you pass to key is
called for each element in the input sequence to
'augment' the list before sorting, as if
you had done:
"""

X =sorted(L, key=lambda t: t[::-1])
print("\n X=")
for w in X : print(w)