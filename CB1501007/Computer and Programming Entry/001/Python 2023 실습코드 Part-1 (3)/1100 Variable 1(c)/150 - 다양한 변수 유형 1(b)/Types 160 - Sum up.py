# 1부터 10까지의 합을 구해봅시다.

i= 1
sum = 0  # 더한 값을 저장하는 변수가 반드시 필요합니데이....
ten = 10

Ml=[]

while ( True ) : #while Loop
    print (" i = ", i, "sum=", sum )
    Ml.append( i )
    sum = sum + i
    i = i + 1
    if i > 10 :
        break



print ("최종 합 sum = ", sum)

print ("최종 List Ml = ", Ml )
