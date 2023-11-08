
s1 = '{0}, {1}, {2}'.format('a', 'b', 'c')

s2 = '{}, {}, {}'.format('a', 'b', 'c')  # 2.7+ only

s3 = '{2}, {1}, {0}, {2}'.format('a', 'b', 'c')

s4 = '{2}, {1}, {0}'.format(*'abc')      # unpacking argument sequence

s5 =  '{0}{1}{0}'.format('abra', 'cad')


print(s1)
print(s2)
print(s3)
print(s4)
print(s5)