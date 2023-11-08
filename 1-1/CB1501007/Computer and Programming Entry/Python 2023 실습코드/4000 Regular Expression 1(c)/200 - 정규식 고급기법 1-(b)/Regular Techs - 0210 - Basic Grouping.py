

import re

txt=  'yasar@webmail.something.edu.tr'
m = re.match( r'([.\w]+)@((\w+)(\.\w+)+)', txt )

print( m.groups() )



