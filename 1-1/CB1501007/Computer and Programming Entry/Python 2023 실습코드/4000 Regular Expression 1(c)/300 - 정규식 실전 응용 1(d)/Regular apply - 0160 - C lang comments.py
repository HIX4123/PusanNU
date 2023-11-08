#
#-------------------------------------------------------------------------------
import re

pattern1 = r'/\*([^*]|[\r\n]|(\*+([^*/]|[\r\n])))*\*+/'
pattern2 = r'//.*?(\r\n?|\n)|(/\*([^*]|[\r\n]|(\*+([^*/]|[\r\n])))*\*+/)'

text='''
 // this is a line comment
void HashDestroy(Hash* hash) {
   /* working
       good
       best example */

    unsigned int i;  // another comments ?
    if (hash == NULL)    return;

    for (i = 0; i < hash->table_size; ++i)     {
  /* this is a comment */
        }
    }
'''

pattobj = re.finditer( pattern1, text)
for mym in pattobj :
    print ("\n -----Pattern 1 찾기 -------- ",)
    print (" 위치 = ", mym.span() ,)
    print (" 매칭부분", mym.group())

print("\n\n 2번째 작업 <<<")

itlist = re.finditer( pattern2, text )
for mym in itlist :
    print ("\n -----Pattern 2 찾기 -------- ",)
    print (" 위치 = ", mym.span() ,)
    print (" 매칭부분", mym.group())