#--------------------------------------------------------
# Author:      Zoh Que
# Created:     30-01-2023
#--------------------------------------------------------

def createGenerator():
    mylist = range(10)
    for i in mylist:
        yield i*i

mygenerator = createGenerator() # create a generator
print(mygenerator) # mygenerator is an object!

for i,val in enumerate(mygenerator):
    print(f"i={i}, val= {val:3}" )

print(f"\n 다시 mygenerator( )를 호출함\n")
for i,val in enumerate(mygenerator):
    print(f"i={i}, val= {val:3}" )



your = createGenerator() # create a generator
print(f"\n 다시 generator를 생성한 후에 다시 호출함\n")
for i,val in enumerate( your ):
    print(f"i={i}, your val= {val:3}" )