
ix, iy= 5,6
matrix = [[]]

# And if you want to generate a matrix of size 5 filled with 0,
matrix = [[0 for i in range(ix)] for i in range(iy)]

matrix[0][0]=87
matrix[0][3]=3
matrix[3][4]=17
matrix[1][2]=33
matrix[4][3]=-9

for w in matrix :
    print(w)



