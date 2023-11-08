
# 3x + 1 Problem




N = 13

Keep=[]

while( N > 1 ):
    Keep.append( N )
    if N%2 == 0 :
        N = int(N/2)
    else:
        N = 3 * N + 1



print("Loop이 끝난 후 \n  ")

for this in Keep :
    print(this)

