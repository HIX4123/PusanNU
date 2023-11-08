#for loop

months =[ 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


for mon, days in enumerate(months) :
    print( mon+1, "월달의 일수", days )

