#for loop


water= [ 45, 34, 12, 9, 23, 65, 23, 54, 66, 75, 2, 14, 15]

Total = 300

given = 0

for w in water :
    if given + w > Total :
        break
    else :
        given = given + w
        print( w, " << 현재까지 공급한 물의 총량: ", given )





