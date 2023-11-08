

sul   = [ 'soju',  'beer', 'baizu', 'wine', 'dansul', 'cognac', 'makgulri',]
anju  = [ 'chicken', 'cheese', 'ozinger', 'sundae', 'taco', 'zokbal']
place = [ 'home',   'outback', 'church', 'classroom', 'beach']

mydrink = [sul, anju, place ]

print("\n Show 01: ", sul[ 0])
print("\n Show 02: ", sul[ 3])
print("\n Show 03: ", sul[-1])
print("\n Show 04: ", sul[-3])

print("\n Show 05: ", mydrink[0][0])
print("\n Show 06: ", mydrink[1])
print("\n Show 07: ", mydrink[-1][-2])

sul.remove("wine")
print("\n Show 08: ", mydrink)

del mydrink[1]
print("\n Show 09: ", mydrink)

a = [1, 2, 3, 4, 2, 3, 4, 2, 7, 2]
a = [x for x in a if x != 2]
print(a)








