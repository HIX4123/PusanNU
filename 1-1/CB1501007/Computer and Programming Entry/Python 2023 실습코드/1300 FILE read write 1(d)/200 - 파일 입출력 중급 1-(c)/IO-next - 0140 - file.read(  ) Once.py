#-------------------------------------------------------------------------------
# Purpose:     2019 Power Python
# Author:      Cho
#-------------------------------------------------------------------------------


# writedata.py
f = open("./data/kukul.txt", 'r')


mydata = f.read( )
print("mydata>>\n", mydata)
print("길이는 = ",  len(mydata))
print("my data의 유형은 ",  type(mydata) )

multiline = mydata.split()
oneline = ''.join( multiline )
print("\noneline = ", len(oneline),"\n>", oneline )

print("\nWho\n")
print("Whom")

f.close()