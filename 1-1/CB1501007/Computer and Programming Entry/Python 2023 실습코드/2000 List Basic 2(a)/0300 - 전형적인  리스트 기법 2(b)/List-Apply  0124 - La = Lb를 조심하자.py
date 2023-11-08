#-------------------------------------------------------------------------------
# Purpose:     2020 Prof. Zoh's Work
# Author:      Cho
# Created:     2020-10-15
#-------------------------------------------------------------------------------

from copy import deepcopy

La = [ 11, 12, 13, 14, 15 ]
Lb = La

print(f"단계 1. La[]=", La )
print(f"단계 2. Lb[]=", Lb )

La.append(100)
print(f"단계 3. La[]=", La )
print(f"단계 4. Lb[]=", Lb )

Lc = deepcopy( La )
La.append(-100)
print(f"단계 5. La[]=", La )
print(f"단계 6. Lc[]=", Lc )

