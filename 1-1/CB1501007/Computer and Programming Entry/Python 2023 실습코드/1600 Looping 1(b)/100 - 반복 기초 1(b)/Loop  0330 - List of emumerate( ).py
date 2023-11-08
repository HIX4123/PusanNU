#for loop

months =[ 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


Month = enumerate( months )

for w in Month:
    print(w)
for w in Month:
    print(f'{w[0]+1:2}월달, 날수={w[1]}')
