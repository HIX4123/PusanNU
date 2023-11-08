import math

myfile = open("facto.txt", "w")

print("교수님이 시킨 일:", file=myfile)

for i in range(10, 21):
    myfile.write(f"{math.factorial(i):25}\n")