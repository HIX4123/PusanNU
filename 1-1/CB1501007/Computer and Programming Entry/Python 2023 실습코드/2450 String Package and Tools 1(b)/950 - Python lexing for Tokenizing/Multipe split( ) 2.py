str = 'Lorem; ipsum. dolor sit amet, consectetur adipiscing elit.'
str = str.split(',')
print(str)

import re
str = 'Lorem; ipsum. dolor sit amet,       consectetur adipiscing elit.'
str = re.split(r' |;|,|\.', str)

nstr = list(filter(lambda a: a != '', str))
print( nstr )