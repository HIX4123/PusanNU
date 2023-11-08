import fileinput

print("Type any words with ^D : ")
for idx, line in enumerate(fileinput.input()):
    print(("i= ", idx, " : ",  line))