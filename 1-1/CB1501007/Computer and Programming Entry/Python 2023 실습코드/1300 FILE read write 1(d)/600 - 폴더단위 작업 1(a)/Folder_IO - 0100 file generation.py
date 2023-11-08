
import os

a = os.getcwd()  # Get Current Working Directory

print(a, len(a))

for x in range(6) :
    name = 'my%03d.txt' % x
    fin  = open(name, "w")
    print((name+" ")*5, file=fin)
    fin.close()


