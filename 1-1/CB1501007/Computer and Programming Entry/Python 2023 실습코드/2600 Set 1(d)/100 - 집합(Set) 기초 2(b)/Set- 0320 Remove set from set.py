

S=[]
s1 =  set( list("Summer Morning") )
s2 =  set( list("Great Evening"))
s3 = s2 - s1
s4 = s1 - s2

S.append ( s1 )
S.append ( s2 )
S.append ( s3  )
S.append ( s4 )

for w in S :
    print(f'set= {w}')
