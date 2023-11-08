#for loop


lmy=[ 34, 56, 2, -43, 56, 12, 23, -50, 5,6, 90, -67, -32]

print( "\n 리스트의 원소를 모두 출력")
for x in lmy :
    print( x + 100 )

print( "\n 리스트의 원소를 index[ ]로 출력")
for i in range(len(lmy)) :
    print(( lmy[i],))


print( "\n 리스트의 원소 일부분을 index[ ]로 출력")
for i in range(5,len(lmy)) :
    print("w=", lmy[i])


