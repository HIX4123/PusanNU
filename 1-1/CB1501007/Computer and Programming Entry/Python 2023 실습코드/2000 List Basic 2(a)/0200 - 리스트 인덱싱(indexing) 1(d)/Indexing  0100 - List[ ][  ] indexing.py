
M    = [ [ 3,   4,  5,  6], \
         [ 6,   8, 10, 12], \
         [ 9,  12, 15, 18], \
         [ 8,  11, 14, 17], \
         [ 12, 16, 20, 24] ]


print("1. ",  M[0]     )
print("2. ",  M[-1]    )
print("3. ",  M[0][2]  )
print("4. ",  M[1][0]  )
print("5. ",  M[2][-1] )
print("6. ",  M[3][ 1] )
print("7. ",  M[-1][-1])


print("row 수=", len(M[0]) )
print("column 수=", len(M) )

for w in range( len(M[0]) ) :
    print( M[w] )

for w in range( len(M) ) :
    print( M[w][2] )




