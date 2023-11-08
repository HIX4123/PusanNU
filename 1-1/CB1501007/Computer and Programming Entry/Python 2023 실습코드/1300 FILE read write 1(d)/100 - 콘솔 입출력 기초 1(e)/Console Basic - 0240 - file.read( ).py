#-------------------------------------------------------------------------------
# Purpose:     2019 Power Python
# Author:      Cho
#-------------------------------------------------------------------------------

# pyscripter 4.0에서 수행되도록 고침

# writedata.py
f = open("./data/kukul.txt", 'r',encoding='cp949')


mydata = f.read( )
print("mydata>> \n", mydata)
print("길이는 = ",  len(mydata))
print("my data의 유형은 ",  type(mydata) )

yourdata = mydata.split()
print("yourdata>> \n", yourdata )



f.close()