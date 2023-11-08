def Remove_vowel( myset ):
    for w in list("aeiou") :
        myset.discard(w)  # remove( )를 사용하면 오

    return( myset )


s1 = set("greatsummertime")
s2 = Remove_vowel( s1 )
print(s2)
s3="".join(s2)
print(s3)
