#-------------------------------------------------------------------------------
# Purpose:     2020 Prof. Zoh's Work
# Author:      Cho
# Created:     2020-06-24
#-------------------------------------------------------------------------------

def Remove_vowel( myset ):
    for w in list("aeiou") :
        myset.discard(w)

    return( myset )


s1 = set("greatsummertime")
s2 = Remove_vowel( s1 )
print(s2)
