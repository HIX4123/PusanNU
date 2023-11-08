

a = 127
b = 31

mok = a // b
rem = a % b
print ("mok=", mok)
print ("rem=", rem)


print ("case 1: ", a/b)
print ("case 2: ", float(a)/b)
print ("case 3: ", float(a/b))
print ("case 4: ", a/float(b))


a = 356.14/14.113
print ("a= ", a)

b = format(a, '.6f')  # formatting

print ("b= ", b)