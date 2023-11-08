#-------------------------------------------------------------------------------
# Purpose:     2020 컴퓨터및 프로그래밍 입문
# Author:      Cho
# Created:     2020-05-14
#-------------------------------------------------------------------------------

# Note that we have not imported any modules

s1 = dir()
print("Step 0>", s1 )


# Now let's import two modules
import random
import math

s2= dir()

print("Step 1>", s2 )
print("Difference S2 - S1>", set(s2)-set(s1) )


