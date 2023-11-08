
word= "Summer Work"
N = len( word )

for x in range(N):
    for y in range(x,N):
        print("Int[",x,",",y,"]=", word[x:y+1] )
