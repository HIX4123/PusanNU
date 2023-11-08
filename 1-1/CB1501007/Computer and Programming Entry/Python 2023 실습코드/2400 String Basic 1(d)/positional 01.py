
a1 = '{0}/{1}/{2}'.format('foo', 'bar', 'baz')
print(a1)
a1=  '{2}.{1}.{0}/{0}{0}.{1}{1}.{2}{2}'.format('foo', 'bar', 'baz')
print(a1)

a1 =  '{x}/{y}/{z}'.format(x='foo', y='bar', z='baz')
print ( a1 )

a1 = '{0}{x}{1}'.format('foo', 'bar', x='baz')
print (a1)

for w in range(100,112):
    print( "1 %r"%w )



print("> form %%r = %r "%([1]))
print("> form %%r = %r "%(32.45))
print("> form %%r = %r "%([1,2,3]))
print("> form %%r = %r "%({3,4,5}))