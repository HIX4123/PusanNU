# Problem Solving Class A
#
# Zoh001.txt Zoh002.txt.... Zoh100.txt

base = "신천쥐"


for i in range(1,101,9) :
    ext= str(i).zfill(3)
    print(ext)
    fname = "data/"+base+"-"+ext+".txt"
    myf = open(fname,"w")
    print("i=", i, file=myf)
    myf.close()  # 반드시 닫아야만 disk에 쓰여진다.