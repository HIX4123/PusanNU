
with open("Wed_Child.txt") as f:
    this = f.read().splitlines()

print ("-------------------\n")
print (this)
print ("-------------------\n")

for i, w in enumerate(this) :
    print (i, ": ", w)


f.close()