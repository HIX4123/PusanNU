#-------------------------------------------------------------------------------
# Author:      Zoh
# Created:     2019-08-29
#-------------------------------------------------------------------------------

with open("m.exe", "rb") as f:
    byte = f.read(1)
    count=0
    while byte != b"":
        byte = f.read(1)
        myb = int.from_bytes( byte , byteorder='big')
        xword = format(myb, 'x') # 숫자를
        print( "%2s" % xword.zfill(2) , end=" ")
        if count % 10 == 0 : print("")
        count+=1

f.close( )