

myset= set()
yourset= set(list("Summer Morning"))
print(f'1> myset = {myset}')

myset.add(10)
myset.add(30)
myset.add(30)
print(f'2> myset = {myset}')

myset.update( list("GoodBoy Man") )
print(f'3> myset = {myset}')
theirset = myset - yourset
print(f'4> theirset = {theirset}')
for w in yourset  :
    if w in set( list("Great Morning In the Evening") ) :
        print(f'{w} in myset')

