import fractions


print("\n 이제 0.1을 계속 10번 더해 봅시다")
#sum = 0.1 + 0.1... +0.1
sum = 0.0
for i in range(10):
     sum += 0.1
     print("i=", i, "sum=", sum)

print(f" sum={sum}, \n sum==1.0인가 {sum==1.0}")

print("\n 이걸 분수로 더해봅시다. ")
fsum = fractions.Fraction(0,10)
for i in range(10):
     fsum += fractions.Fraction(1,10)
     print("i=", i, "fsum=", fsum)


print(f" fsum={fsum}, \n fsum==1.0인가 {fsum==1}")

