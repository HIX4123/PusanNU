

import  re

txt= "내가 좋아하는 바지는 그리고 싫어하는 스타일 바지는\
      최애하는 모자는 이것이고 짱나는 신발은 저것이고\
      간지나는  abc  간지나는  좋아한 잠바는 THG 좋을것 같은"


L1 = r"좋\w+\b"

print( re.findall( L1, txt ) )


L2 = r"좋\w+[ ]+(\w+)"
print( re.findall( L2, txt ) )




