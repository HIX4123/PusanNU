
L = [ 3, 4, [5, 6, 7], 9, [ 10, 2], 9]


for w in L :
    if type(w) == type( list() ) :       ## most preferred way to check if it's list
        print("이것은 List의 첫 원소 = ", w[0] )


for w in L :
    if isinstance( w, list):              ## most preferred way to check if it's list
        print("이것은 List = ", w )

