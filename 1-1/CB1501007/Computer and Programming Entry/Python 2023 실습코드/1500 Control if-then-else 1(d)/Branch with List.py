

Return=["VOL", "FACE", "LINE", "POINT", "NULL"]
L= [ [2, 2, 2],[1, 2, 2],[1, 1, 2], [1, 1, 1]]

Q=[1,2,2]

def findme(X):
    if X in L :
        return (L.index(X) )
    else :
        return (4)


print( Return[ findme(Q) ] )
print( Return[ findme([4,5,6]) ] )