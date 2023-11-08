#-------------------------------------------------------------------------------
# Purpose:     2019 Power Python
# Author:      Cho
#-------------------------------------------------------------------------------


# writedata.py
f = open("./data/kukul.txt", 'r')


mydata = f.read( )
print("mydata>> \n", mydata)
print("길이는 = ",  len(mydata))
print("my data의 유형은 ",  type(mydata) )

yourdata = mydata.split()
print("yourdata>> \n", yourdata )



f.close()