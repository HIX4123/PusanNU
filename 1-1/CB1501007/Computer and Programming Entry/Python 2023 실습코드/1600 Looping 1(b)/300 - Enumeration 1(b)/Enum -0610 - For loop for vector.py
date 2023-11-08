
lx = [("Dog", "Cat"), ("Beer", "Peanut"),("Soju", "Fork"),("Bus", "Taxi"),("10", "11"), ]


N = set ( a for a, b in lx )
print(N)

M = list ( b for a, b in lx )
print(M)