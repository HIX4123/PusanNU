
class My :
    cvar = 999
    def __init__(self):
        self.x = 0
        self.cvar = 100

    def plusone(self):
        self.x += 1
        self.cvar += 1


    def showx( self ):
        print(("In My( ): x = ", self.x, self.cvar ))



a = My()
print((My.cvar))
print((a.x, a.cvar))
a.plusone()
a.plusone()
a.plusone()
a.plusone()
a.showx()