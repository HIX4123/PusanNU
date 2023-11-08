

# 우리는 n X m 2차원 행렬(격자)를 만든다.
# n은 column의 크기이며 m은 row의 크기이다.

n, m = 5, 4

matrix=[]
for arow in range(m):
    x = [0]*n
    matrix.append(x)


matrix[0][0]=99
matrix[3][2]=17
matrix[2][4]=-6

for i,w in enumerate(matrix) :
    print("row=",i, w)
