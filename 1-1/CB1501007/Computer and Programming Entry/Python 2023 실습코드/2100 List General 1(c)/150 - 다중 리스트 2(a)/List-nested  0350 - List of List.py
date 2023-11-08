

m=[[5,4,3], [7,8,9], [11,12,13]]
print(m[0], m[1])
print(m[1][1])

#실험 1 - Matrix 출력
print("실험 1. \n")
for x in range( len(m[0])):
    for y in range( len(m[x-1])):
        print("%4d" % m[x][y], end=' ')
    print("\n", end=' ')


#실험 2 - List안의 List
s1 = ["good", "old", "NewYork", "'boy"]
s2 = ["Brennt", "Paris ? "]
s3 = ["easier", "said", "than", "done" ]
s4 =  ["alles good"]

blk = [s1, s2, s3, s4]
print(blk, len(blk))


print("\n After s2 modified")
s1[2] = "Something"
s2[0] = "Crazzzzy"
s3 = []
print(blk)

nested =[0]
print(nested)
origin = [ nested, 1]
print(origin)
nested = 'Cool Guy'
print(origin)     #수정이 되지 않음 (생성과 참조의 차이)