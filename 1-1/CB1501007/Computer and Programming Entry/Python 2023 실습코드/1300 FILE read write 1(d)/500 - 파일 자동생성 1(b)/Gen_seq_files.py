#-------------------------------------------------------------------------------
# Author:      Zoh
# Created:     2020-09-20
#-------------------------------------------------------------------------------

# List L의 내용을 파일 이름 fname으로 만듬
# 따라서 만들 파일을 반드시 List로 미리 만들어야 함.

def Gen_Seq_Files( fname, L ) :
    myfile = open( fname, "w")
    for aline in L :
        for w in aline :
            print(w, end=" ", file= myfile)
        print(file= myfile)
    myfile.close( )


Content=[ [1,2,3], [45, 78], [99], [ ], [0, 1, 2, 3, 4]]


N= 10  # 만들 데이터 개수
base  = "./myfile/Zoh"
for w in range(1,N):
    namein  = base+"_in_" +str(w).zfill(2)+".txt"
    nameout = base+"_out_"+str(w).zfill(2)+".txt"
    Gen_Seq_Files( namein,  Content )
    Gen_Seq_Files( nameout, Content )