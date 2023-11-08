#for loop


s = 0
for x in range(100) :
    s = s + x
    print("x=", x, "s=", s)
    if s > 200 :
        break

exit(0)

s = 0
i= 1
while( 1 ):
    i = i + 1
    s = s + i
    if s > 200 :
        break
    print("==>", i, s )


