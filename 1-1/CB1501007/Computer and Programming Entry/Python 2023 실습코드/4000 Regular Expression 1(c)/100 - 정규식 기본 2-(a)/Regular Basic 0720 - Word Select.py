
import re

text = """
One summer got night
The stars were shining bright
One Summer Summers pot
Made with fancy whims but
That summers night
567  45.678 0.345
My whole world tumbled down
I could have died, if not for you
"""

# Summer류의 단어 혹은 끝이 t로 끝나는 2글자이상의 단어

copr = r'[Ss]ummers?|(\w{2,}t)'
#패턴에서 앞에 있는 선언이 먼저 매칭된다.

plist = re.findall( copr, text )

print("\n plist[]= ", plist)

plist = re.finditer( copr, text )

for w in plist :
    print( f' w.group()={w.group():10}, w.group(1)= {w.group(1)}')



