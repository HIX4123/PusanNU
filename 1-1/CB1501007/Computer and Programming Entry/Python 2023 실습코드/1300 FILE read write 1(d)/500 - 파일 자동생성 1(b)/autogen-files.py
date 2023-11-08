#-------------------------------------------------------------------------------
# Author:      Zoh
# Created:     2020-09-20
#-------------------------------------------------------------------------------

# 데이터 만들기 Template

N= 15  # 만들 데이터 개수
base  = "./CafeData/cafe1"

def genfile( fname, L ) :
    myfile = open( fname, "w")
    for aline in L :
        for w in aline :
            print(w, end=" ", file= myfile)
        print(file= myfile)
    myfile.close( )


Content=[ [1,2,3], [45, 78], [99], [0, 1, 2, 3, 4]]

for w in range(1,6):
    namein  = base+"_in" +str(w).zfill(2)+".txt"
    nameout = base+"_out"+str(w).zfill(2)+".txt"


    genfile( namein, Content )