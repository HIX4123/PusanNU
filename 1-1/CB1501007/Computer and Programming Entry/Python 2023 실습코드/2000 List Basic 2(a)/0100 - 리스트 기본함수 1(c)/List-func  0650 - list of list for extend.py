
tem = [[] for x in range(10) ]

la = [3, 5, 11]

print(tem)

tem[2].append(55)
print(tem)

tem[8].extend( la )
print(tem)