
People=[ 36534, 12345, 24565, 13489, 18737, 24565,
   38173, 30987, 23445, 11390, 30098, 29987, 16800, 18345, 23097]




def sexsplit( L ) :
    Male  =[]
    Female=[]
    Child =[]   # Male=Child=Female=[]
    for w in L :
        rsex = w//10000
        if rsex == 2 : Female.append( w )
        if rsex == 1 :   Male.append( w )
        if rsex == 3 :   Child.append( w )
    return( Male, Female, Child )




A, B, C = sexsplit( People)
print(f" 남성 집단 ={A}")
print(f" 여성 집단 ={B}")
print(f" 어린이 집단 ={C}")



