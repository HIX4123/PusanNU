#-------------------------------------------------------------------------------
# Purpose:     2019 Power Python
# Author:      Cho
#-------------------------------------------------------------------------------


class Example:
    def __init__( self, big, number, small):
        self.big = big
        self.number = number
        self.small = small

    def wout( self ) :
        print( "Example=", self.big, self.number, self.small)



Lobj = [ Example('A', 3, 'a'), Example('R', 1, 'q'), Example('C', 2, 'c'), \
         Example('T', 9, 'e'), Example('W', 7, 'm'), Example('H', 5, 'z') ]

# 정렬
Lobj.sort(key = lambda object : object.number)


print( Lobj )

for w in Lobj :
    w.wout()