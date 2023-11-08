
la = [1, 2,    4,            9, 10]
lb = [      3, 4, 5, 6, 7, 8,   10]

lor  = la or lb
land = la and lb

lxor = set(la)^set(lb)




print("lor=" , lor)
print("land=",land)
print("lxor=", list(lxor) )