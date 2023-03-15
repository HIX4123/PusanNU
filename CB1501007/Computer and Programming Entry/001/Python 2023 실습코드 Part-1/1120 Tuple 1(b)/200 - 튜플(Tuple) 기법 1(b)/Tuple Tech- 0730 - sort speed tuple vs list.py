import random
from timeit import Timer

def set_data(N):
    Tlist=[]
    Llist=[]
    for w in range(N):
        ns = random.randrange(1,20)
        Newl=[]
        for q in range( ns ) :
            val = random.randrange(100)
            Newl.append(val)
        Llist.append( Newl )
        Tlist.append( tuple(Newl))

    return( Tlist, Llist)

A,B = set_data(100)
#print(f"\n A={A}")
#print(f"\n B={B}")

def Asort( ):
    global A
    A.sort()
    return

def Bsort( ):
    global B
    B.sort()
    return



t_listTest = Timer( Asort )
print( f"List element sort( ) 시간 : {t_listTest.timeit():10.7}")


t_tupleTest = Timer( Bsort )
print( f"Tuple element sort( ) 시간 : {t_tupleTest.timeit():10.7}")
