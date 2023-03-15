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


print(f" sum= {sum}, \n 총합은 1인가 ? {sum==1.0}")


print("\n 이제 0.11을 계속 10번 더해 봅시다")
sum = 0.0
for i in range(10):
     sum += 0.11
     print("i=", i, "sum=", sum)
print(f" sum= {sum}, \n 총합은 1.1인가 ? {sum==1.1}")

print("\n 이제 0.31을 계속 100번 더해 봅시다")
sum = 0.0
for i in range(100):
     sum += 0.31

print(f" sum= {sum}, \n 총합은 31인가 ? {sum==31}")




