#-------------------------------------------------------------------------------
# Author:      Zoh
# Created:     2020-04-12
#-------------------------------------------------------------------------------

import datetime
date = datetime.date(1991, 10, 12)

m1 = f'{date} was on a {date:%A}'
print(m1)

m2 = f'The date is {date:%A, %B %d, %Y}.'
print(m2)
