#-------------------------------------------------------------------------------
# Purpose:     2019 Power Python
# Author:      Cho
#-------------------------------------------------------------------------------



print("\n 이제 0.1을 계속 10번 더해 봅시다")
#sum = 0.1 + 0.1
sum = 0.0
for i in range(10):
     sum += 0.1
     print("i=", i, "sum=", sum)


print("Sum=", sum)
if sum == 0.9 :  print("Yes, Sum  = 0.9")
else :           print("Np,  Sum != 0.9")

